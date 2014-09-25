# coding: utf-8
from django.conf.urls import patterns, url

from esperancanordeste.catalog.views import (ProductListView,
                                             ProductCategoryListView,
                                             ProductDetailListView)


urlpatterns = patterns(
    'esperancanordeste.catalog.views',
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        ProductCategoryListView.as_view(),
        name='category_list'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$',
        ProductDetailListView.as_view(),
        name='product_detail'),
)
