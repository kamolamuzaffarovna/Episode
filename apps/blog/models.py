from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from utils.make_slugify import make_slugify


class BaseModel(models.Model):
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(BaseModel):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(BaseModel):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=221)
    slug = models.SlugField(max_length=221, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Blog)
def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        make_slugify(instance)



