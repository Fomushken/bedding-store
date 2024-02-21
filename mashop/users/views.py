from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shop.utils import DataMixin
from users.forms import LoginForm, RegisterUserForm


# Create your views here.


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    title_page = 'Authorization'


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    title_page = 'Registration'
    success_url = reverse_lazy('users:login')