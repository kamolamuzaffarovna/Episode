from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    search_fields = ('name', )
    date_hierarchy = 'created_date'
