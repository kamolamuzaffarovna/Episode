from django.shortcuts import render

from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'contact/login.html'


class LogoutView(TemplateView):
    template_name = 'contact/logout.html'


class RegisterView(TemplateView):
    template_name = 'contact/register.html'
