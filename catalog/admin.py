from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published')
    list_filter = ('category', 'published')
    search_fields = ('title', 'body', 'sidebar_text')
    exclude = ('slug',)
