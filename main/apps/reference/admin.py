from django.contrib import admin

from .models import Reference


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'solver', 'sector', 'category']
    list_filter = ['sector']
    search_fields = ['titel', 'owner__last_name']
