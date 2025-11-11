from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("display_user", "message", "timestamp", "is_admin")
    list_filter = ("is_admin", "timestamp")
    search_fields = ("message", "visitor_name")

    def display_user(self, obj):
        if obj.is_admin:
            return "Admin"
        return obj.visitor_name or "Ziyaretçi"

    display_user.short_description = "Gönderen"
