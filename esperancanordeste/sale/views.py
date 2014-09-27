# coding: utf-8
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views import generic

from esperancanordeste.context_processors import (EnterpriseExtraContext,
                                                  enterprise_proc)

from esperancanordeste.sale.models import (Area, Seller, Segment)
from esperancanordeste.core.models import STATE_CHOICES

from esperancanordeste.sale.forms import ContactForm


def home(request):
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

    segment = request.GET.get('segment', '')
    state = request.GET.get('state', '')
    if segment and state:
        seller_list = Seller.published.filter(
            Q(segment__name__icontains=segment), Q(state__icontains=state))
    elif segment:
        seller_list = Seller.published.filter(
            Q(segment__name__icontains=segment))
    elif state:
        seller_list = Seller.published.filter(
            Q(state__icontains=state))
    else:
        seller_list = Seller.published.all()

    context['segment'] = segment
    context['state'] = state
    context['area_list'] = Area.objects.all()[:1]
    context['seller_list'] = seller_list
    context['segment_list'] = Segment.objects.all()
    context['state_list'] = STATE_CHOICES

    return render(request, 'sale/sale_home.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


class SaleFormView(EnterpriseExtraContext, generic.FormView):
    form_class = ContactForm
    success_url = "/area/"
    template_name = "sale/sale_home.html"

    def get_context_data(self, **kwargs):
        context = super(SaleFormView, self).get_context_data(**kwargs)

        segment = self.request.GET.get('segment', '')
        state = self.request.GET.get('state', '')
        if segment and state:
            seller_list = Seller.published.filter(
                Q(segment__name__icontains=segment), Q(state__icontains=state))
        else:
            seller_list = Seller.published.all()

        context['segment'] = segment
        context['state'] = state
        context['area_list'] = Area.objects.all()[:1]
        context['seller_list'] = seller_list
        context['segment_list'] = Segment.objects.all()
        context['state_list'] = STATE_CHOICES

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form.send_mail()
        context['contact_success'] = True
        return super(SaleFormView, self).form_valid(form)