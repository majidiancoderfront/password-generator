from django.contrib import admin
from .models import GeneratedPassword


@admin.register(GeneratedPassword)
class GeneratedPasswordAdmin(admin.ModelAdmin):
    list_display = ['password', 'length', 'include_uppercase', 'include_lowercase', 'include_numbers', 'include_symbols', 'created_at']
    list_filter = ['include_uppercase', 'include_lowercase', 'include_numbers', 'include_symbols', 'created_at']
    search_fields = ['password']
    readonly_fields = ['created_at']
