from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from esperancanordeste.core.views import (HomeListView, BrandListView)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'esperancanordeste.core.views.home', name='home'),
    # url(r'^$', HomeListView.as_view(), name='home'),
    url(r'^contato/', 'esperancanordeste.core.views.contact', name='contact'),
    url(r'^institucional/', 'esperancanordeste.core.views.institutional',
        name='institutional'),
    url(r'^pedido/', 'esperancanordeste.core.views.order', name='order'),
    url(r'^marcas/', BrandListView.as_view(), name='brand'),

    url(r'^campanhas/', include('esperancanordeste.campain.urls',
        namespace='campain')),
    url(r'^catalogo/', include('esperancanordeste.catalog.urls',
        namespace='catalog')),
    url(r'^vendas/', include('esperancanordeste.sale.urls',
        namespace='sale')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
