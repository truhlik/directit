from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'time_duration', 'price', 'milestone']
    search_fields = ['name']
    list_filter = ['milestone', 'category']
