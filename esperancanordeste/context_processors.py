# coding: utf-8
from django.shortcuts import get_object_or_404

from esperancanordeste.core.models import Enterprise, SocialLogo
from esperancanordeste.catalog.models import Category
from esperancanordeste.newsletter.models import Subscribe
from esperancanordeste.newsletter.forms import SubscribeForm


def enterprise_proc(request):
    """ View Function """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    social_list = SocialLogo.objects.all()
    category_list = Category.objects.all()

    # newsletter
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            obj = Subscribe.objects.filter(email=form.cleaned_data['email'])
            if not obj:
                form.save()
                subscribe_success = True
                subscribe_exist = False
            else:
                subscribe_exist = True
                subscribe_success = False
    else:
        form = SubscribeForm()
        subscribe_success = False
        subscribe_exist = False

    return {
        'enterprise': enterprise,
        'social_list': social_list,
        'cat_list': category_list,
        'newsletter_form': form,
        'subscribe_success': subscribe_success,
        'subscribe_exist': subscribe_exist,
    }


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

    def get_context_data(self, **kwargs):
        context = super(EnterpriseExtraContext,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
