from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(_(u'Nome'), max_length=30)
    slug = models.SlugField(_(u'Slug'), max_length=30, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')
        ordering = ['name']
