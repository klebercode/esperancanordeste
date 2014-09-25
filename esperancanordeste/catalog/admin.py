from django.contrib import admin

from esperancanordeste.catalog.models import (Catalog, Category, Product)


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('created', 'name', 'admin_attach')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('admin_image', 'name', 'category', 'visible')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
