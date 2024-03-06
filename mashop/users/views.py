from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView

from users.forms import UserPasswordChangeForm
from shop.utils import DataMixin
from users.forms import LoginForm, RegisterUserForm, ChangeProfileUserForm


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

class ProfileUser(DataMixin, LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


class ChangeProfileUser(DataMixin, UpdateView):
    template_name = 'users/change_profile_user.html'
    model = get_user_model()
    form_class = ChangeProfileUserForm

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:password_change_done')
    form_class = UserPasswordChangeForm
