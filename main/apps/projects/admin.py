from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Project
from main.apps.files.models import File
from main.libraries.functions import get_absolute_url


class ProjectFileForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = File.projects.through
        fields = ['file', 'project', 'title']

    def __init__(self, *args, **kwargs):
        super(ProjectFileForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = 'Title'


class FilesInlineAdmin(admin.TabularInline):
    model = File.projects.through
    extra = 0

    readonly_fields = ['title', 'description', 'file_url']
    exclude = ['file']
    verbose_name = 'Soubor'
    verbose_name_plural = 'Soubory'

    def has_add_permission(self, request, obj):
        return False

    def title(self, instance):
        return instance.file.title
    title.short_description = 'title'

    def description(self, instance):
        return instance.file.description
    description.short_description = 'description'

    def file_url(self, instance):
        url = get_absolute_url(instance.file.file.url)
        return mark_safe('<a href="{}" download>stáhnout</a>'.format(url))
    description.short_description = 'URL'


class FilesAddInline(admin.StackedInline):
    model = File.projects.through
    extra = 1

    verbose_name = 'Soubor'
    verbose_name_plural = 'Soubory'

    def has_view_or_change_permission(self, request, obj=None):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'name', 'description', 'updated_at', 'created_at']
    list_filter = ['updated_at', 'created_at']
    search_fields = ['name', 'categories__name']
    autocomplete_fields = ['consultant']
    inlines = [FilesInlineAdmin, FilesAddInline]
    exclude = ['files', ]
