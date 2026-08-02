from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'slug')
    list_filter = ('published',)
    search_fields = ('title', 'teaser', 'body')
    date_hierarchy = 'published'
    ordering = ('-published',)
    exclude = ('slug',)
