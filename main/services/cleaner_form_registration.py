from main.models import *
from myusers.models import UsersModel
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def clean_all(request) -> dict:
    """Валидность формы регистрации"""
    if 'username' in request.POST:
        status, text = clean_username(username=request.POST['username'])
        return {'success': status, 'text': text}
    elif 'email' in request.POST:
        status, text = clean_email(email=request.POST['email'])
        return {'success': status, 'text': text}
    elif 'password2' in request.POST:
        status, text = clean_passwords(request.POST['password1'], request.POST['password2'])
        return {'success': status, 'text': text}
    return {'success': True, 'text': 'OK'}


def clean_username(username):
    """Валидность username`а"""
    if len(username) < 3 or len(username) > 150:
        return False, 'Логин должен быть от 3 до 150 символов'
    elif username.isdigit():
        return False, 'Логин не может быть числом'
    elif UsersModel.objects.filter(username=username):
        return False, 'Логин уже занят'
    return True, 'OK'


def clean_email(email):
    """Валидность email`а"""
    try:
        validate_email(email)
    except ValidationError:
        return False, 'Введите адрес электронной почты'
    else:
        if not UsersModel.objects.filter(email=email):
            return True, 'OK'
        else:
            return False, 'Этот Email уже используется'


def clean_passwords(password1, password2):
    """Валидность пароля"""
    if len(password1) < 8:
        return False, 'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'
    elif password1.isdigit():
        return False, 'Введённый пароль состоит только из цифр'
    elif password1 != password2:
        return False, 'Пароли не совпадают'
    return True, 'OK'
