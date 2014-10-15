# coding: utf-8
from django.db.models import Q
from django.views import generic
# from django.views.generic.dates import (YearArchiveView, MonthArchiveView,
#                                         DayArchiveView)

from esperancanordeste.context_processors import EnterpriseExtraContext

from esperancanordeste.catalog.models import Catalog, Category, Product


class ProductListView(EnterpriseExtraContext,  generic.ListView):
    queryset = Product.published.all()
    template_name = 'catalog/catalog_home.html'
    # TODO: mudar a paginacao para 20
    paginate_by = 20

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        if search:
            obj_lst = Product.published.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search))
        else:
            obj_lst = Product.published.all()
        return obj_lst

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search', '')
        context['search'] = search
        context['category_list'] = Category.objects.all()
        context['catalog_list'] = Catalog.objects.all()
        return context


class ProductCategoryListView(ProductListView):
    """
    Herda de EntryListView mudando o filtro para tag selecionada
    """
    def get_queryset(self):
        """
        Incluir apenas as Entries marcadas com a tag selecionada
        """
        return Product.published.filter(
            category__slug=self.kwargs['category_slug'])


class ProductDetailListView(ProductListView):
    """
    Herda de EntryListView mudando o filtro para tag selecionada
    """
    template_name = 'catalog/catalog_detail.html'

    def get_queryset(self):
        """
        Incluir apenas as Entries marcadas com a tag selecionada
        """
        return Product.published.filter(
            category__slug=self.kwargs['category_slug'],
            slug=self.kwargs['slug'])
