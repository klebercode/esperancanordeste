# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SubscribeAllManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Entry sem filtros
    """
    def get_queryset(self):
        return super(SubscribeAllManager,
                     self).get_queryset().all()


class SubscribeReceiveManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Entry que estao marcados
    como publish=True
    """
    def get_queryset(self):
        return super(SubscribeReceiveManager,
                     self).get_queryset().filter(receive=True)


class Subscribe(models.Model):
    email = models.EmailField(_(u'Descrição'))
    receive = models.BooleanField(_(u'Receber Newsletter?'), default=True)

    objects = SubscribeAllManager()
    receives = SubscribeReceiveManager()

    def __unicode__(self):
        return unicode(self.email)

    class Meta:
        verbose_name = _(u'Inscrição')
        verbose_name_plural = _(u'Inscrições')
        ordering = ['email']
