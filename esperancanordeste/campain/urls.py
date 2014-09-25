# coding: utf-8
from django.conf.urls import patterns, url

from esperancanordeste.campain.views import (EntryListView, EntryTagListView,
                                             EntryDetailListView)


urlpatterns = patterns(
    'esperancanordeste.campain.views',
    url(r'^$', EntryListView.as_view(), name='home'),
    url(r'^(?P<slug>[-\w]+)/$', EntryDetailListView.as_view(),
        name='entry_detail'),
    url(r'^marcacao/(?P<tag_slug>[-\w]+)/$', EntryTagListView.as_view(),
        name='tag_list'),
)
