# coding: utf-8
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views import generic
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormMixin
from django.contrib import messages

from esperancanordeste.context_processors import (EnterpriseExtraContext,
                                                  enterprise_proc)

from esperancanordeste.core.models import (Order, Step, Institutional,
                                           Timeline, PhotoInstitutional,
                                           Brand, Partner, Banner)
from esperancanordeste.catalog.models import (Category, Product)
from esperancanordeste.newsletter.models import (Subscribe)
from esperancanordeste.campain.models import (Entry)

from esperancanordeste.core.forms import ContactForm
from esperancanordeste.newsletter.forms import SubscribeForm


class SubscribeFormView(generic.FormView):
    def form_valid(self, form):
        form.save()
        return super(SubscribeFormView, self).form_valid(form)


def home(request):
    context = {}
    context['step_list'] = Step.objects.all()
    context['banner_list'] = Banner.published.all()
    context['partner_list'] = Partner.objects.all().order_by('?')
    context['campain_list'] = Entry.published.filter(
        categories__category='campanha')

    categoryargs = Category.objects.all().order_by('?')[:4]

    product_list = Product.published.filter(
        category__name__in=list(categoryargs[:4])).order_by('category')

    context['product_list'] = product_list

    search = request.GET.get('search', '')
    if search:
        context['search'] = search

    return render(request, 'home.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))


class HomeListView(EnterpriseExtraContext, FormMixin, generic.ListView):
    model = Step
    template_name = 'home.html'
    form_class = SubscribeForm

    # def get_queryset(self, **kwargs):
        # email = self.request.GET.get('email', '')
        # if email:
        #     obj = Subscribe.objects.get_or_create(email=email)

        # search = self.request.GET.get('search', '')
        # if search:
        #     obj_lst = Entry.published.filter(Q(title__icontains=search) |
        #                                      Q(created__icontains=search) |
        #                                      Q(body__icontains=search))
        # else:
        #     obj_lst = Entry.published.all()
        # return obj_lst

    def get_success_message(self):
        return 'Obrigado!<br>Email cadastrado com sucesso.'

    def get_success_url(self, **kwargs):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        # context = super(HomeListView, self).get_context_data(**kwargs)
        # if not request.user.is_authenticated():
        #     return HttpResponseForbidden()
        # self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            # return self.form_invalid(form)
            return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        obj = Subscribe.objects.filter(email=form.cleaned_data['email'])
        if not obj:
            form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             self.get_success_message())
        return super(HomeListView, self).form_valid(form)
        # return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        # search = self.request.GET.get('search', '')
        # context['search'] = search
        context['step_list'] = Step.objects.all()
        context['partner_list'] = Partner.objects.all().order_by('?')
        context['campain_list'] = Entry.published.filter(
            categories__category='campanha')
        context['categ_list'] = Category.objects.all().order_by('?')[:4]
        context['product_list'] = Product.published.all().order_by('?')[:24]
        context['banner_list'] = Banner.published.all()
        form_class = self.get_form_class()
        context['newsletter_form'] = self.get_form(form_class)
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
    if request.method == 'POST' and 'contact' in request.POST:
        contact_form = ContactForm(request.POST, prefix='Contact')
        if contact_form.is_valid():
            contact_form.send_mail()
            context['contact_success'] = True
    else:
        contact_form = ContactForm()

    context['contact_form'] = contact_form

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


class BrandListView(EnterpriseExtraContext,  generic.ListView):
    queryset = Brand.objects.all()[:1]
    template_name = 'brand.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['partner_list'] = Partner.objects.all()
        return context
