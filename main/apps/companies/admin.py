from django.contrib import admin

from .models import Company, UserCompany


class UserCompanyInline(admin.TabularInline):
    model = UserCompany
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'phone', 'web', 'reg_number', 'vat_number', 'get_address']
    list_filter = ['role']
    search_fields = ['name', 'email', 'reg_number']
    inlines = [UserCompanyInline]
    autocomplete_fields = ['categories', 'tags']

    def get_address(self, obj):
        return obj.address
