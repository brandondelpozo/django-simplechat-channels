from django.urls import path

from chat_profile.views import share_profile

urlpatterns = [
    path("chat_profile/<int:pk>/share/", share_profile, name="share-profile"),
]