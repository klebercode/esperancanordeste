# coding: utf-8
from django.contrib import admin

from esperancanordeste.sale.models import (Area, Segment, Phone, Email, Seller)


class SellerAdmin(admin.ModelAdmin):
    list_filter = ('segment__name', 'state')
    list_display = ('name', 'state', 'get_phone', 'get_email')
    search_fields = ('name', 'state',)

    # define the raw_id_fields
    raw_id_fields = ('phone', 'email', 'segment')
    # define the autocomplete_lookup_fields
    autocomplete_lookup_fields = {
        'm2m': ['phone', 'email', 'segment'],
    }


class AreaAdmin(admin.ModelAdmin):
    list_display = ('admin_description',)
    search_fields = ('admin_description',)


admin.site.register(Seller, SellerAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Segment)
admin.site.register(Phone)
admin.site.register(Email)
