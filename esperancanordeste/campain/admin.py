# coding: utf-8
from django.contrib import admin

from mce_filebrowser.admin import MCEFilebrowserAdmin

from esperancanordeste.campain.models import Entry, Category


class EntryAdmin(MCEFilebrowserAdmin):
    list_filter = ('created', 'author__username', 'categories')
    list_display = ('title', 'created', 'author', 'publish')
    search_fields = ('title', 'created', 'author', 'body')
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
