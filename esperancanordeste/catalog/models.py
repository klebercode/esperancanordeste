# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from sorl.thumbnail import ImageField
from esperancanordeste.fields import ContentTypeRestrictedFileField

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps


class Catalog(models.Model):
    created = models.DateTimeField(_(u'Data de Envio'), auto_now_add=True)
    name = models.CharField(_(u'Nome para o Catálogo'), max_length=50,
                            help_text='Catálogo 2014')
    attach = ContentTypeRestrictedFileField(
        _(u'Arquivo'),
        upload_to=u'catalog',
        content_types=['application/pdf', 'application/zip'],
        max_upload_size=5242880,
        help_text=u'Selecione um arquivo com tamanho máximo de 5MB.')

    def admin_attach(self):
        if self.attach:
            return "<a href='%s'>Baixar</a>" % self.attach.url
        else:
            return "Nenhum arquivo encontrado."
    admin_attach.allow_tags = True
    admin_attach.short_description = _(u'Arquivo')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Catálogo')
        verbose_name_plural = _(u'Catálogos')
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField(_(u'Nome'), max_length=30)
    slug = models.SlugField(_(u'Link'), max_length=30, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')
        ordering = ['name']


class ProductAllManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Catalog sem filtros
    """
    def get_queryset(self):
        return super(ProductAllManager,
                     self).get_queryset().all()


class ProductPublishedManager(models.Manager):
    """
    Esse manager carrega todos os objetos do model Catalog que estao marcados
    como visible=True
    """
    def get_queryset(self):
        return super(ProductPublishedManager,
                     self).get_queryset().filter(visible=True)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_(u'Categoria'))
    name = models.CharField(_(u'Nome'), max_length=120,
                            help_text='Nome do produto')
    slug = models.SlugField(_(u'Link'), max_length=50, unique=True)
    description = models.TextField(_(u'Descrição'), max_length=250,
                                   help_text='Descrição do produto')
    image = ImageField(_(u'Imagem'), upload_to=u'product',
                       help_text='Tamanho: 800x640 px (Ideal)')
    visible = models.BooleanField(_(u'Visível no site?'), default=True)

    # quando precisar chamar todos os objetos sem filtro:
    # Product.objects.all()
    objects = ProductAllManager()
    # quando precisar chamar apenas os objetos com visible=True:
    # Product.published.all()
    published = ProductPublishedManager()

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def save(self, *args, **kwargs):
        if not self.id and not self.image:
            return

        super(Product, self).save(*args, **kwargs)

        image = Image.open(self.image)

        def scale_dimensions(width, height, longest_side):
            if width > height:
                if width > longest_side:
                    ratio = longest_side*1./width
                    return (int(width*ratio), int(height*ratio))
                elif height > longest_side:
                    ratio = longest_side*1./height
                    return (int(width*ratio), int(height*ratio))
            return (width, height)

        (width, height) = image.size
        (width, height) = scale_dimensions(width, height, longest_side=800)

        size = (width, height)
        """ redimensiona esticando """
        # image = image.resize(size, Image.ANTIALIAS)
        """ redimensiona proporcionalmente """
        image.thumbnail(size, Image.ANTIALIAS)
        """ redimensiona cortando para encaixar no tamanho """
        # image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image.save(self.image.path, 'JPEG', quality=99)

    def get_absolute_url(self):
        return reverse('catalog:product_detail',
                       kwargs={'category_slug': slugify(self.category.slug),
                               'slug': slugify(self.slug)})

    def __unicode__(self):
        return '%s - %s' % (unicode(self.category),
                            unicode(self.name))

    class Meta:
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'Produtos')
        ordering = ('name',)
