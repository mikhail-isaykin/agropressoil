from django.contrib import admin
from .models import Category, Product, Part


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')
    list_filter = ('product',)
