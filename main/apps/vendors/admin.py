from django.contrib import admin

from main.apps.vendors.models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
