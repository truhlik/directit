from django.contrib import admin

from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['categories']
    search_fields = ['name']
    autocomplete_fields = ['categories']
