from django.urls import path

from .views import EmailLoginView
from sesame.views import LoginView

urlpatterns = [
    path("login/", EmailLoginView.as_view(), name="email_login"),
    path("login/auth/", LoginView.as_view(), name="login"),
]
