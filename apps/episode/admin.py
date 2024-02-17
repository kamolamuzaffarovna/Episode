from django.contrib import admin
from .models import Episode, Comment, EpisodeLike, EpisodeFilter


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'slug', 'created_date')
    readonly_fields = ('created_date', 'slug', 'modified_date')
    date_hierarchy = 'created_date'
    search_fields = ('title', )
    list_filter = ('category', 'tags')
    filter_horizontal = ('tags', 'filter')
    autocomplete_fields = ('author', )
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    date_hierarchy = 'created_date'
    autocomplete_fields = ('episode', )
    search_fields = ('author', )


@admin.register(EpisodeLike)
class EpisodeLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'episode')
    search_fields = ('episode', )
    autocomplete_fields = ('episode', 'author')


admin.site.register(EpisodeFilter)