from django.shortcuts import render
from .models import Category, Tag
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog


class BlogListView(ListView):
    queryset = Blog.objects.all()[:3]


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()

    def get_categories(self):
        return Category.objects.all()

    def get_tags(self):
        return Tag.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = self.get_categories()
        ctx['tags'] = self.get_tags()

        return ctx
