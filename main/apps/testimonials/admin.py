from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['owner', 'company', 'rating', 'text', 'authorized']
    list_filter = ['authorized']
