# coding: utf-8
from django import forms

from esperancanordeste.newsletter.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        exclude = ('receive',)
