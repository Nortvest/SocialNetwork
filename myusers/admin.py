from django.contrib import admin
from .models import UsersModel


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name',
                    'email', 'is_superuser', 'is_staff', 'last_login')
    list_display_links = ('id', 'username')


admin.site.register(UsersModel, UsersAdmin)
