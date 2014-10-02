# coding: utf-8
from django.conf.urls import patterns, url

# from esperancanordeste.sale.views import (SaleFormView, EstimateFormView)
                                             # ProductCategoryListView,
                                             # ProductDetailListView)


urlpatterns = patterns(
    'esperancanordeste.sale.views',
    url(r'^area/', 'home', name='home'),
    url(r'^orcamento/', 'estimate', name='estimate'),
    # url(r'^area/', SaleFormView.as_view(), name='home'),
    # url(r'^orcamento/', EstimateFormView.as_view(), name='estimate'),
    # url(r'^(?P<category_slug>[-\w]+)/$',
    #     ProductCategoryListView.as_view(),
    #     name='category_list'),
    # url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$',
    #     ProductDetailListView.as_view(),
    #     name='product_detail'),
)
