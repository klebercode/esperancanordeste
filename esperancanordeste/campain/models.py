# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager

from esperancanordeste.current_user import get_current_user


class EntryManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Entry sem filtros
    """
    def get_queryset(self):
        return super(EntryManager,
                     self).get_queryset().all()


class PublishedManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Entry que estao marcados
    como publish=True
    """
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(publish=True)


class Entry(models.Model):
    title = models.CharField(_(u'Título da Campanha'), max_length=200)
    slug = models.SlugField(_(u'Link no Site'), max_length=200,
                            unique=True)
    image = ImageField(_(u'Imagem'), upload_to='campain', blank=True,
                       null=True)
    video = EmbedVideoField(_(u'Vídeo'), blank=True, null=True)
    body = tinymce_models.HTMLField(_(u'Texto'))
    publish = models.BooleanField(_(u'Publicar no site?'), default=True)
    created = models.DateTimeField(_(u'Data de Criação'), auto_now_add=True)
    modified = models.DateTimeField(_(u'Data de Modificação'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_(u'Autor'),
                               editable=False, default=get_current_user)

    tags = TaggableManager()
    # quando precisar chamar todos os objetos sem filtro:
    # Entry.objects.all()
    objects = EntryManager()
    # quando precisar chamar apenas os objetos com publish=True:
    # Entry.published.all()
    published = PublishedManager()

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('campain:entry_detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Campanha')
        verbose_name_plural = _(u'Campanhas')
        ordering = ['-created', 'title', 'author']
