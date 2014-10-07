# coding: utf-8
from django.shortcuts import render
from django.template import RequestContext

from esperancanordeste.context_processors import enterprise_proc

from esperancanordeste.newsletter.forms import SubscribeForm


def subscribe(request):
    context = {}

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            context['newsletter_success'] = True
    else:
        form = SubscribeForm()

    context['newsletter_form'] = form

    return render(request, 'newsletter_subscribe.html', context,
                  context_instance=RequestContext(request,
                                                  processors=[enterprise_proc]
                                                  ))
