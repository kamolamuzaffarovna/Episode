from django.shortcuts import render
from .models import Episode
from django.views.generic import TemplateView, DetailView, ListView


class EpisodeListView(ListView):
    queryset = Episode.objects.all()
    template_name = 'episode/episode_list.html'


class EpisodeDetailView(DetailView):
    queryset = Episode.objects.all()
    slug_field = "slug"
    template_name = 'episode/episode_detail.html'


class EpisodePlaylist(TemplateView):
    template_name = 'episode/playlist.html'
