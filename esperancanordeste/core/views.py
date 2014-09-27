# coding: utf-8
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views import generic

from esperancanordeste.context_processors import (EnterpriseExtraContext,
                                                  enterprise_proc)

from esperancanordeste.core.models import (Order, Step, Institutional,
                                           Timeline, PhotoInstitutional,
                                           Brand, Partner)
from esperancanordeste.catalog.models import (Category)

from esperancanordeste.core.forms import ContactForm


class HomeListView(EnterpriseExtraContext,  generic.ListView):
    model = Step
    template_name = 'home.html'

    # def get_queryset(self, **kwargs):
    #     search = self.request.GET.get('search', '')
    #     if search:
    #         obj_lst = Entry.published.filter(Q(title__icontains=search) |
    #                                          Q(created__icontains=search) |
    #                                          Q(body__icontains=search))
    #     else:
    #         obj_lst = Entry.published.all()
    #     return obj_lst

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        # search = self.request.GET.get('search', '')
        # context['search'] = search
        context['step_list'] = Step.objects.all()
        return context


def institutional(request):
    context = {}
    context['institutional_list'] = Institutional.objects.all()[:1]
    context['timeline_list'] = Timeline.objects.all()
    context['photo_list'] = PhotoInstitutional.objects.all()

    return render(request, 'institutional.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def contact(request):
    context = {}

    # contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            context['contact_success'] = True
    else:
        form = ContactForm()

    context['contact_form'] = form

    return render(request, 'contact.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


def order(request):
    context = {}
    context['order_list'] = Order.objects.all()[:1]

    return render(request, 'order.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


# TODO: depende do cliente para definir os campos
# ticket id: #4411428
def estimate(request):
    context = {}

    return render(request, 'estimate.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


class BrandListView(EnterpriseExtraContext,  generic.ListView):
    queryset = Brand.objects.all()[:1]
    template_name = 'brand.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['partner_list'] = Partner.objects.all()
        print context
        return context
