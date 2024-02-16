from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from .models import Comment, Tag, Category, Episode, EpisodeLike


class EpisodeListView(ListView):
    queryset = Episode.objects.all()
    template_name = 'episode/episode_list.html'


class EpisodeDetailView(TemplateView):
    template_name = 'episode/episode_detail.html'

    def get_tag(self):
        return Tag.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_comment(self):
        return Comment.objects.filter()             #episode=self.get_episode(), parent__isnull=True

    def get_episode(self):
        return Episode.objects.all()

    def get_likes(self):
        return EpisodeLike.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tags'] = self.get_tag()
        ctx['categories'] = self.get_category()
        ctx['comments'] = self.get_comment()
        ctx['episodes'] = self.get_episode()
        ctx['likes'] = self.get_likes()

        return ctx


class EpisodePlaylist(TemplateView):
    template_name = 'episode/playlist.html'
