from django.contrib import admin
from .models import CallBackRequest


@admin.register(CallBackRequest)
class CallBackRequestAdmin(admin.ModelAdmin):
    fields = ['callback_type', 'user', 'name', 'phone', 'time', 'note']
    list_filter = ['callback_type']
    search_fields = ['name', 'phone', 'note']
