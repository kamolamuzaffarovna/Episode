from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from apps.episode.models import Episode


class HomeView(ListView):
    queryset = Episode.objects.all()[:3]
    template_name = 'core/index.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(CreateView):
    """
    {app_name}/{model_name}_form
    """
    form_class = ContactForm
    model = Contact
    success_url = reverse_lazy('core:contact')

