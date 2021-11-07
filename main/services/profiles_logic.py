from myusers.models import UsersModel
from main.models import *


def get_fullname(user_pk: int) -> str:
    name = UsersModel.objects.values('first_name', 'last_name').get(pk=user_pk)
    return f'{name["first_name"]} {name["last_name"]}'


def get_user_posts(user_pk):
    return PostsModel.objects.filter(own__pk=user_pk)


def get_user_data(user_pk):
    return UsersModel.objects.get(pk=user_pk)
