from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, ListView
from .models import Comment, Tag, Category, Episode, EpisodeLike, EpisodeFilter
from .. import episode


class EpisodeListView(ListView):
    queryset = Episode.objects.all()
    paginate_by = 1

    def get_tag(self):
        return Tag.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_filter(self):
        return EpisodeFilter.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tags'] = self.get_tag()
        ctx['categories'] = self.get_category()
        ctx['filter'] = self.get_filter()

        return ctx


class EpisodeDetailView(TemplateView):
    template_name = 'episode/episode_detail.html'

    def get_tag(self):
        return Tag.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_comment(self):
        return Comment.objects.filter()                        #episode=self.get_episode(), parent__isnull=True

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

    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')
        pid = request.GET.get('pid')
        if message:
            instance = self.get_episode()
            user = request.user
            Comment.objects.create(episode_id=instance.id, author_id=user.id, parent_id=pid, message=message)
            return redirect('.#comments')
        messages.error(request, "Comment is empty")
        return redirect('.')



class EpisodePlaylist(TemplateView):
    template_name = 'episode/playlist.html'
