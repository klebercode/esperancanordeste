# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import TabularInline, StackedInline

from esperancanordeste.sale.models import (Area, Segment, Phone, Email, Seller,
                                           Estimate)


class EmailInline(TabularInline):
    model = Email
    extra = 1


class PhoneInline(TabularInline):
    model = Phone
    extra = 1


class SellerAdmin(admin.ModelAdmin):
    list_filter = ('segment__name', 'state')
    list_display = ('name', 'state', 'get_phone', 'get_email')
    search_fields = ('name', 'state',)
    inlines = [EmailInline, PhoneInline]
    # # define the raw_id_fields
    # raw_id_fields = ('phone', 'email', 'segment')
    # # define the autocomplete_lookup_fields
    # autocomplete_lookup_fields = {
    #     'm2m': ['phone', 'email', 'segment'],
    # }


class AreaAdmin(admin.ModelAdmin):
    list_display = ('admin_description',)
    search_fields = ('admin_description',)


class EstimateAdmin(admin.ModelAdmin):
    list_filter = ('segment', 'city', 'district', 'state')
    list_display = ('created', 'segment', 'enterprise', 'cnpj', 'name')
    search_fields = ('segment', 'enterprise', 'cnpj', 'name')


admin.site.register(Seller, SellerAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Estimate, EstimateAdmin)
admin.site.register(Segment)
admin.site.register(Phone)
admin.site.register(Email)
