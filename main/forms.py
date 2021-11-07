from django import forms
from myusers.models import UsersModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    """Форма для Регистрации"""
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Логин'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Пароль'}))


class RegisterForm(UserCreationForm):
    """Форма для Аутентификации"""
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Придумайте логин'}))
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Имя'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Фамилия'}))
    email = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Почта'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Придумайте пароль'}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Повторите пароль'}))
    photo = forms.ImageField(label='Аватар',
                             required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UsersModel
        fields = ('username', 'first_name', 'last_name', 'email', 'photo')
