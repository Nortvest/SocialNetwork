from django.contrib import admin
from .models import *


class TypeMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_media')


class PostsAdmin(admin.ModelAdmin):
    list_display = ('text', 'media', 'own', 'type_media')


class LikesAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'user')


class FollowersAdmin(admin.ModelAdmin):
    list_display = ('user', 'user2')


admin.site.register(TypeMediaModel, TypeMediaAdmin)
admin.site.register(PostsModel, PostsAdmin)
admin.site.register(LikesModel, LikesAdmin)
admin.site.register(CommentsModel, CommentsAdmin)
admin.site.register(FollowersModel, FollowersAdmin)
