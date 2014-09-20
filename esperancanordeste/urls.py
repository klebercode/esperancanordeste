from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from esperancanordeste.core.views import HomeListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', 'esperancanordeste.core.views.home', name='home'),
    url(r'^$', HomeListView.as_view(), name='home'),
    url(r'^contato/', 'esperancanordeste.core.views.contact', name='contact'),
    url(r'^institucional/', 'esperancanordeste.core.views.institutional',
        name='institutional'),
    url(r'^pedido/', 'esperancanordeste.core.views.order', name='order'),
    url(r'^orcamento/', 'esperancanordeste.core.views.estimate',
        name='estimate'),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
