from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'created_at', 'updated_at']
    list_filter = ['updated_at']
    search_fields = ['name']
