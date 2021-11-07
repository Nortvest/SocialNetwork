from django.shortcuts import redirect
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login, mixins
from main.forms import *
from main.services.cleaner_form_registration import clean_all
from main.services.profiles_logic import get_fullname, get_user_posts, get_user_data
from main.utils import AuthMixin
from django.http import JsonResponse


class AuthView(AuthMixin, LoginView):
    """Представление Вохда"""
    form_class = LoginForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['btn_text'] = 'Войти'
        context['active'] = 0
        return context

    @staticmethod
    def get_success_url():
        return reverse_lazy('profile')


class RegistrationView(AuthMixin, CreateView):
    """Представление создания аккаунта"""
    form_class = RegisterForm
    template_name = 'main/login.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['btn_text'] = 'Зарегистрироваться'
        context['active'] = 1
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class ValidRegistrationView(FormView):
    """Обработка AJAX для форсы регистрации"""
    form = RegisterForm

    def post(self, request, *args, **kwargs):
        return JsonResponse(clean_all(request))


def logout_view(request):
    """Выход из аккаунта"""
    logout(request)
    return redirect('login')


class ProfileView(mixins.LoginRequiredMixin, TemplateView):
    """Представление профиля пользоателя"""
    template_name = 'main/profile.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мой профиль'
        context['user_data'] = get_user_data(self.request.user.pk)
        context['fill_name'] = get_fullname(self.request.user.pk)
        posts = get_user_posts(self.request.user.pk)
        context['posts'] = posts
        context['count_posts'] = 1 and posts.count() > 1 or 0
        return context
