# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

import datetime
now = datetime.datetime.now()

from esperancanordeste.fields import MonthYearWidget
from esperancanordeste.core.models import Timeline


class ContactForm(forms.Form):
    name = forms.CharField(label=u'Nome',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Nome'}))
    phone = forms.CharField(label=u'Fone',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Fone'}))
    email = forms.EmailField(label=u'E-mail',
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'E-mail'}))
    subject = forms.CharField(label=u'Assunto',
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control',
                                         'placeholder': 'Assunto'}))
    message = forms.CharField(label=u'Mensagem',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'rows': 3,
                                         'placeholder': 'Mensagem'}))

    def send_mail(self):
        subject = u'Contato do site (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'phone': self.cleaned_data['phone'],
            'email': self.cleaned_data['email'],
            'subject': self.cleaned_data['subject'],
            'message': self.cleaned_data['message'],
        }
        message = render_to_string('contact_mail.txt', context)
        message_html = render_to_string('contact_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     'no-reply@esperancanordeste.com.br',
                                     # ['contato@rhape.com.br']
                                     ['kleberss@gmail.com'])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()


class TimelineForm(forms.ModelForm):
    period = forms.DateField(
        label=u'Período',
        widget=MonthYearWidget(years=xrange(1980, now.year+1)))

    class Meta:
        model = Timeline
