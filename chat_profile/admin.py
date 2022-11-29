from django.contrib import admin
from django.utils.html import format_html

from .models import ChatProfile

@admin.register(ChatProfile)
class ChatProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "customer", "private_sharing_link"]
    
    def private_sharing_link(self, obj):
        return format_html('<a href="{}">Link</a>', obj.get_private_sharing_link())
    
    