from django.urls import path
from django.conf.urls.static import static
from SocialNetwork import settings
from main.views import *

urlpatterns = [
    path('', AuthView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('registration/validation_of_login_or_registration', ValidRegistrationView.as_view(),
         name='validation_of_login_or_registration')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
