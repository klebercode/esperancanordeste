# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import TabularInline, StackedInline

from esperancanordeste.core.models import (Enterprise, Social, SocialLogo,
                                           Order, Step, Institutional,
                                           Timeline, PhotoInstitutional,
                                           Brand, Partner)


class SocialLogoInline(TabularInline):
    model = SocialLogo
    extra = 1


class SocialAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    inlines = [SocialLogoInline]


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'phone3', 'email')
    search_fields = ('name', 'description', 'address', 'number', 'complement',
                     'cep', 'district', 'city', 'state',
                     'phone1', 'phone2', 'phone3', 'email')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('admin_body',)
    search_fields = ('body',)


class StepAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


class TimelineInline(StackedInline):
    model = Timeline
    extra = 1


class PhotoInstitutionalInline(StackedInline):
    model = PhotoInstitutional
    extra = 1


class InstitutionalAdmin(admin.ModelAdmin):
    list_display = ('admin_description',)
    search_fields = ('description',)
    inlines = [TimelineInline, PhotoInstitutionalInline]


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'category__name')


class PartnerInline(StackedInline):
    model = Partner
    extra = 1


class BrandAdmin(admin.ModelAdmin):
    list_display = ('admin_description',)
    search_fields = ('description',)
    inlines = [PartnerInline]


admin.site.register(Social, SocialAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Institutional, InstitutionalAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Brand, BrandAdmin)
