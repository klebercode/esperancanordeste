# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from tinymce import models as tinymce_models

from esperancanordeste.core.models import STATE_CHOICES


OPERATOR_CHOICES = (
    (1, _(u'Fixo')),
    (2, _(u'Claro')),
    (3, _(u'Oi')),
    (4, _(u'Nextel')),
    (5, _(u'Tim')),
    (6, _(u'Vivo')),
    (99, _(u'Outra')),
)


class Area(models.Model):
    description = tinymce_models.HTMLField(_(u'Descrição da página'))

    def admin_description(self):
        return self.description
    admin_description.allow_tags = True
    admin_description.short_description = _(u'Descrição da página')

    def __unicode__(self):
        return unicode(self.description)

    class Meta:
        verbose_name = _(u'Descrição da Página')
        verbose_name_plural = _(u'Descrição da Página')
        ordering = ['-id']


class Segment(models.Model):
    name = models.CharField(_(u'Nome do Segmento'), max_length=50, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)

    class Meta:
        verbose_name = _(u'Segmento')
        verbose_name_plural = _(u'Segmentos')
        ordering = ['name']


class Phone(models.Model):
    operator = models.IntegerField(_(u'Operadora'), choices=OPERATOR_CHOICES)
    number = models.CharField(_(u'Número'), max_length=20,
                              help_text='(99) 9999-9999')
    default = models.BooleanField(_(u'Número principal?'))

    @staticmethod
    def autocomplete_search_fields():
        return ("number__icontains", "operator__icontains",)

    def __unicode__(self):
        return unicode(self.number)

    class Meta:
        verbose_name = _(u'Fone')
        verbose_name_plural = _(u'Fones')
        ordering = ['-default']


class Email(models.Model):
    address = models.EmailField(_(u'Endereço de email'))
    default = models.BooleanField(_(u'Email principal?'))

    @staticmethod
    def autocomplete_search_fields():
        return ("address__icontains",)

    def __unicode__(self):
        return unicode(self.address)

    class Meta:
        verbose_name = _(u'Email')
        verbose_name_plural = _(u'Emails')
        ordering = ['-default', 'address']


class SellerAllManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Entry sem filtros
    """
    def get_queryset(self):
        return super(SellerAllManager,
                     self).get_queryset().all()


class SellerPublishedManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Entry que estao marcados
    como publish=True
    """
    def get_queryset(self):
        return super(SellerPublishedManager,
                     self).get_queryset().filter(visible=True)


class Seller(models.Model):
    area = models.ForeignKey(Area, verbose_name=_(u'Página'), blank=True,
                             null=True)
    name = models.CharField(_(u'Nome'), max_length=150, unique=True)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    segment = models.ManyToManyField(Segment, verbose_name=_(u'Segmento'))
    phone = models.ManyToManyField(Phone, verbose_name=_(u'Fone'))
    email = models.ManyToManyField(Email, verbose_name=_(u'Email'))
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    objects = SellerAllManager()
    published = SellerPublishedManager()

    def get_phone(self):
        out = []
        for k in self.phone.all():
            out.append('%s<br>' % k.number)
        return '\n'.join(out)
    get_phone.allow_tags = True
    get_phone.short_description = _(u'Fones')

    def get_email(self):
        out = []
        for k in self.email.all():
            out.append('%s<br>' % k.address)
        return '\n'.join(out)
    get_email.allow_tags = True
    get_email.short_description = _(u'Emails')

    def save(self, *args, **kwargs):
        check = Area.objects.all()[:1]
        if not check:
            a = Area(description=u"Aguardando conteúdo...")
            a.save()
            self.area = a
        else:
            self.area = check[0]
        super(Seller, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Vendedor')
        verbose_name_plural = _(u'Vendedores')
        ordering = ['name', 'state']
