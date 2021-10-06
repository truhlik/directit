from django.contrib import admin

from main.apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    autocomplete_fields = ['suppliers', 'categories', 'tags', 'vendor']
