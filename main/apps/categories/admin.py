from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    search_fields = ['name']
