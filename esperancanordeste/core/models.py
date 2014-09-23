# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from sorl.thumbnail import ImageField
from tinymce import models as tinymce_models

import datetime
now = datetime.datetime.now()

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps

from esperancanordeste.catalog.models import Category


STATE_CHOICES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)

ICON_CHOICES = (
    ('fa-truck', _(u'Caminhão')),
    ('fa-download', _(u'Baixar')),
    ('fa-edit', _(u'Orçamento')),
)

PAGE_CHOICES = (
    ('pedido', _(u'Pedido')),
    ('orcamento', _(u'Orçamento')),
)


class Social(models.Model):
    description = models.CharField(_(u'Descrição'), max_length=120,
                                   help_text='Breve texto para a área social')

    def __unicode__(self):
        return unicode(self.description)

    class Meta:
        verbose_name = _(u'Social')
        verbose_name_plural = _(u'Social')
        ordering = ['description']


class SocialLogo(models.Model):
    social = models.ForeignKey('Social', verbose_name=_(u'Social'))
    name = models.CharField(_(u'Nome'), max_length=50,
                            help_text='Nome da Instituição')
    image = models.ImageField(_(u'Logo'), upload_to='social',
                              help_text='Tamanho Ideal 115x100 px')
    link = models.URLField(_(u'Site'), blank=True, null=True,
                           help_text='Ex: http://www.instituicao.com.br/')

    def admin_image(self):
        return '<img src="%s" width="115" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Logo da Instituição'

    def save(self, *args, **kwargs):
        if not self.id and not self.image:
            return

        super(SocialLogo, self).save(*args, **kwargs)

        image = Image.open(self.image)
        (width, height) = image.size

        # if (100 / width < 100 / height):
        #     factor = 100 / height
        # else:
        #     factor = 100 / width

        # size = (width / factor, height / factor)
        size = (115, 100)
        """ redimensiona esticando """
        # image = image.resize(size, Image.ANTIALIAS)
        """ redimensiona proporcionalmente """
        # image.thumbnail(size, Image.ANTIALIAS)
        """ redimensiona cortando para encaixar no tamanho """
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image.save(self.image.path, 'JPEG', quality=99)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Social Logo')
        verbose_name_plural = _(u'Social Logos')
        ordering = ['name']


class Enterprise(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    description = models.CharField(_(u'Descrição'), max_length=100,
                                   blank=True, null=True)
    cnpj = models.CharField(_(u'CNPJ'), max_length=20,
                            help_text='99.999.999/9999-99')
    address = models.CharField(_(u'Endereço'), max_length=200)
    number = models.CharField(_(u'Número'), max_length=10)
    complement = models.CharField(_(u'Complemento'), max_length=100,
                                  blank=True, null=True)
    cep = models.CharField(_(u'CEP'), max_length=9, help_text='99999-999',
                           blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100)
    city = models.CharField(_(u'Cidade'), max_length=100)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    country = models.CharField(_(u'País'), max_length=50)
    phone1 = models.CharField(_(u'Fone 1 (Televendas)'), max_length=20,
                              help_text='(99) 9999-9999')
    phone2 = models.CharField(_(u'Fone 2'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    phone3 = models.CharField(_(u'Fone 3 (Fax)'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    email = models.EmailField(_(u'Email'))
    site = models.URLField(_(u'Site'))

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Empresa')
        verbose_name_plural = _(u'Empresa')


class Order(models.Model):
    body = tinymce_models.HTMLField(_(u'Informações'))

    def admin_body(self):
        return self.body
    admin_body.allow_tags = True
    admin_body.short_description = _(u'Informações')

    def __unicode__(self):
        return unicode(self.body)

    class Meta:
        verbose_name = _(u'Receba seu Pedido')
        verbose_name_plural = _(u'Receba seu Pedido')


class Step(models.Model):
    title = models.CharField(_(u'Título'), max_length=21)
    description = models.CharField(_(u'Descrição'), max_length=90)
    page = models.CharField(_(u'Página'), max_length=20, choices=PAGE_CHOICES,
                            blank=True, null=True)
    link = models.URLField(_(u'Link para site externo'), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Caixa da Home')
        verbose_name_plural = _(u'Caixas da Home')


class Institutional(models.Model):
    description = tinymce_models.HTMLField(_(u'Descrição da página'))

    def admin_description(self):
        return self.description
    admin_description.allow_tags = True
    admin_description.short_description = _(u'Descrição da página')

    def __unicode__(self):
        return unicode(self.description)

    class Meta:
        verbose_name = _(u'Institucional')
        verbose_name_plural = _(u'Institucional')


class Timeline(models.Model):
    institutional = models.ForeignKey('Institutional',
                                      verbose_name=_(u'Institucional'))
    title = models.CharField(_(u'Título'), max_length=50)
    description = models.TextField(_(u'Descrição'),
                                   help_text='Uma breve história')
    image = ImageField(_(u'Imagem'), upload_to='institutional/timeline',
                       blank=True, null=True)
    period = models.CharField(_(u'Ano'), max_length=4, unique=True,
                              help_text=now.year)

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def __unicode__(self):
        return "%s (%s)" % (unicode(self.title), self.period)

    class Meta:
        verbose_name = _(u'Linha do Tempo')
        verbose_name_plural = _(u'Linha do Tempo')
        ordering = ['period']


class PhotoInstitutional(models.Model):
    institutional = models.ForeignKey('Institutional',
                                      verbose_name=_(u'Institucional'))
    title = models.CharField(_(u'Título da Imagem'), max_length=50)
    description = models.CharField(_(u'Descrição'), max_length=200,
                                   blank=True, null=True)
    image = ImageField(_(u'Imagem'), upload_to='institutional/photos')

    def admin_image(self):
        return '<img src="%s" width="160" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Foto')
        verbose_name_plural = _(u'Fotos')


class Brand(models.Model):
    page = models.CharField(_(u'Nome da página'), max_length=20,
                            default='Marcas', editable=False)
    description = tinymce_models.HTMLField(_(u'Descrição da página'))

    def admin_description(self):
        return self.description
    admin_description.allow_tags = True
    admin_description.short_description = _(u'Descrição da página')

    def __unicode__(self):
        return unicode(self.page)

    class Meta:
        verbose_name = _(u'Marca')
        verbose_name_plural = _(u'Marcas')


class Partner(models.Model):
    brand = models.ForeignKey('Brand', verbose_name=_(u'Página'), default=1,
                              blank=True, null=True)
    name = models.CharField(_(u'Nome'), max_length=30)
    image = ImageField(_(u'Imagem'), upload_to='brand')
    category = models.ManyToManyField(Category, verbose_name='Categorias')

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def save(self, *args, **kwargs):
        check = Brand.objects.all()[:1]
        if not check:
            b = Brand(description=u"Aguardando conteúdo...")
            b.save()
            self.brand = b
        super(Partner, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Parceiro')
        verbose_name_plural = _(u'Parceiros')
