import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        this_year = datetime.date.today().year
        fields = ['username', 'date_birth', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'date_birth': forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-10)))
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('This email exists already')
        return email


class ChangeProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    date_birth = forms.DateField(disabled=True, label='Date of birth')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'date_birth', 'first_name', 'last_name']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs=
                                                                                              {'class': 'form-input'}))
