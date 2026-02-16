from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(MultipleSubmit)
class MultipleSubmitAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribe',]
    search_fields = ['email']