# coding: utf-8
from django.conf.urls import patterns, url

# from esperancanordeste.sale.views import (SaleFormView)
                                             # ProductCategoryListView,
                                             # ProductDetailListView)


urlpatterns = patterns(
    'esperancanordeste.sale.views',
    url(r'^$', 'home', name='home'),
    # url(r'^$', SaleFormView.as_view(), name='home'),
    # url(r'^(?P<category_slug>[-\w]+)/$',
    #     ProductCategoryListView.as_view(),
    #     name='category_list'),
    # url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$',
    #     ProductDetailListView.as_view(),
    #     name='product_detail'),
)
