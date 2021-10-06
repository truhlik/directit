from django.contrib import admin

from .models import Software


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'licence_count', 'licence_till', 'find_alternative', 'watch_expiration',
                    'need_extension', 'need_customization', 'need_upgrade']
    list_filter = ['find_alternative', 'watch_expiration', 'need_extension', 'need_customization', 'need_upgrade']
    search_fields = ['owner__last_name', 'owner__email', 'name']
    autocomplete_fields = ['categories']
