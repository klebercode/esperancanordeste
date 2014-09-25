# coding: utf-8
from django.shortcuts import get_object_or_404

from esperancanordeste.core.models import Enterprise, SocialLogo


def enterprise_proc(request):
    """ View Function """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    social_list = SocialLogo.objects.all()

    return {
        'enterprise': enterprise,
        'social_list': social_list,
    }


class EnterpriseExtraContext(object):
    """ Class Based View """
    try:
        enterprise = get_object_or_404(Enterprise, pk=1)
    except:
        enterprise = ''

    social_list = SocialLogo.objects.all()

    extra_context = {
        'enterprise': enterprise,
        'social_list': social_list,
    }

    def get_context_data(self, **kwargs):
        context = super(EnterpriseExtraContext,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
