from django.conf import settings
from django.db import models
from django.urls import reverse

from sesame.utils import get_query_string

class ChatProfile(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def get_private_sharing_link(self):
        link = reverse("share-profile", args=(self.pk,))
        link += get_query_string(user=self.customer, scope=f"chat_profile:{self.pk}")
        return link
    