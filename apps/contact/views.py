from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import auth_logout
from django.views.generic import TemplateView, View
from .forms import UserRegisterForm
from .models import ProfilePicture


class LoginView(TemplateView):
    template_name = 'contact/login.html'


class LogoutView(View):
    template_name = 'contact/logout.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('/')


class RegisterView(View):
    template_name = 'contact/register.html'
    form_class = UserRegisterForm

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if request.FILES:
                ProfilePicture.objects.create(user=user, picture=request.FILES.get('image'))
                messages.success(request, "Successfully registered")
        return redirect(reverse_lazy('contact:login'))
