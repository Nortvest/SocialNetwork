from django.shortcuts import redirect


class AuthMixin:
    """Mixin для редиректа аутентифицированного пользователя"""
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().get(request, *args, **kwargs)
