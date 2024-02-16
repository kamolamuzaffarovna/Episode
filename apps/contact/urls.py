from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import LoginView, LogoutView, RegisterView

app_name = 'contact'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='contact/login.html',
                                                next_page=reverse_lazy('core:home')), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]
