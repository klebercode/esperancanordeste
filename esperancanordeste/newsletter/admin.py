# coding: utf-8
from django.contrib import admin

from esperancanordeste.newsletter.models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_filter = ('receive',)
    list_display = ('email', 'receive')
    search_fields = ('email',)


admin.site.register(Subscribe, SubscribeAdmin)
