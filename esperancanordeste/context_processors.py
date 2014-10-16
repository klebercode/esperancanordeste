# coding: utf-8
from django.shortcuts import get_object_or_404

from esperancanordeste.core.models import Enterprise, SocialLogo
from esperancanordeste.catalog.models import Category
from esperancanordeste.newsletter.models import Subscribe

from esperancanordeste.newsletter.forms import SubscribeForm


def enterprise_proc(request):
    """ View Function """
    context = {}

    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    social_list = SocialLogo.objects.all()
    category_list = Category.objects.all()

    # newsletter
    if request.method == 'POST' and 'subscribe' in request.POST:
        newsletter_form = SubscribeForm(request.POST, prefix='Subscribe')
        if newsletter_form.is_valid():
            obj = Subscribe.objects.filter(
                email=newsletter_form.cleaned_data['email'])
            if not obj:
                newsletter_form.save()
                context['subscribe_success'] = True
            else:
                context['subscribe_exist'] = True
    else:
        newsletter_form = SubscribeForm(prefix='Subscribe')

    context['enterprise'] = enterprise
    context['social_list'] = social_list
    context['cat_list'] = category_list
    context['newsletter_form'] = newsletter_form

    return context


class EnterpriseExtraContext(object):
    """ Class Based View """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    social_list = SocialLogo.objects.all()
    category_list = Category.objects.all()

    extra_context = {
        'enterprise': enterprise,
        'social_list': social_list,
        'cat_list': category_list,
    }

    def process_request(self, request):
        extra_context = {}
        # newsletter
        if request.method == 'POST' and 'subscribe' in request.POST:
            newsletter_form = SubscribeForm(request.POST, prefix='Subscribe')
            if newsletter_form.is_valid():
                obj = Subscribe.objects.filter(
                    email=newsletter_form.cleaned_data['email'])
                if not obj:
                    newsletter_form.save()
                    extra_context['subscribe_success'] = True
                else:
                    extra_context['subscribe_exist'] = True
        else:
            newsletter_form = SubscribeForm(prefix='Subscribe')

    def get_context_data(self, **kwargs):
        context = super(EnterpriseExtraContext,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
