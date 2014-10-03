# coding: utf-8
from django.db.models import Q
from django.views import generic
# from django.views.generic.dates import (YearArchiveView, MonthArchiveView,
#                                         DayArchiveView)

from esperancanordeste.context_processors import EnterpriseExtraContext

from esperancanordeste.campain.models import Entry, Category


class EntryListView(EnterpriseExtraContext,  generic.ListView):
    queryset = Entry.published.all()
    template_name = 'campain/campain_home.html'
    # TODO: mudar a paginacao para 10
    paginate_by = 5

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        if search:
            obj_lst = Entry.published.filter(Q(title__icontains=search) |
                                             Q(created__icontains=search) |
                                             Q(body__icontains=search))
        else:
            obj_lst = Entry.published.all()
        return obj_lst

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        search = self.request.GET.get('search', '')
        context['search'] = search
        context['category_list'] = Category.objects.all()
        return context


class EntryTagListView(EntryListView):
    """
    Herda de EntryListView mudando o filtro para tag selecionada
    """
    def get_queryset(self):
        """
        Incluir apenas as Entries marcadas com a tag selecionada
        """
        return Entry.published.filter(
            categories__category=self.kwargs['cat_slug'])


class EntryDetailListView(EntryListView):
    """
    Herda de EntryListView mudando o filtro para tag selecionada
    """
    template_name = 'campain/campain_detail.html'

    def get_queryset(self):
        """
        Incluir apenas as Entries marcadas com a tag selecionada
        """
        return Entry.published.filter(slug=self.kwargs['slug'])
