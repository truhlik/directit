from django.contrib import admin

from .models import Message, MessageThread


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(MessageThread)
class MessageThreadAdmin(admin.ModelAdmin):
    pass

