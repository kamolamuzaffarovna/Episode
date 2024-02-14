from django.contrib import admin
from .models import (
    Category,
    Tag,
    Blog
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    search_fields = ('title', )
    readonly_fields = ('created_date', 'modified_date')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'slug', 'created_date')
    readonly_fields = ('created_date', 'slug', 'modified_date')
    date_hierarchy = 'created_date'
    search_fields = ('title', 'author')
    # autocomplete_fields = ('author', )
    filter_horizontal = ('tags', )
