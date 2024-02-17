import os
from django.db.models import Q

from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe

from apps.blog.models import BaseModel, Category, Tag
from utils.make_slugify import make_slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class EpisodeFilter(BaseModel):
    filter = models.CharField(max_length=221)
    display = models.CharField(max_length=221)

    def __str__(self):
        return self.display

    def safe_filter(self):
        return self.filter[1:]


class Episode(BaseModel):
    title = models.CharField(max_length=221)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='episode/')
    filter = models.ManyToManyField(EpisodeFilter, limit_choices_to=~Q(filter="*"))
    music = models.FileField(upload_to='episodes/', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    slug = models.SlugField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="50" height="50" /></a>')
        return '-'

    @property
    def music_absolute_path(self):
        return self.music.url


class Comment(BaseModel):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comment/')
    message = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    @property
    def get_children(self):
        model = self.__class__
        return model.objects.filter(top_level_comment_id=self.id)


class EpisodeLike(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


@receiver(pre_save, sender=Episode)
def episode_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        make_slugify(instance)


@receiver(pre_save, sender=Comment)
def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if not instance.parent.top_level_comment_id:
            instance.parent.top_level_comment_id = instance.parent_id
        else:
            instance.top_level_parent_id = instance.parent.top_level_comment_id