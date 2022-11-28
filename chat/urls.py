# chat/urls.py
from django.urls import path
from sesame.views import LoginView

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("sesame/login/", LoginView.as_view(), name="sesame-login"),
]