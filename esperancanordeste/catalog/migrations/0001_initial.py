# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        return
        # # Adding model 'Catalog'
        # db.create_table(u'catalog_catalog', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        #     ('attach', self.gf('esperancanordeste.fields.ContentTypeRestrictedFileField')(max_length=100)),
        # ))
        # db.send_create_signal(u'catalog', ['Catalog'])

        # # Adding model 'Category'
        # db.create_table(u'catalog_category', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        #     ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=30)),
        # ))
        # db.send_create_signal(u'catalog', ['Category'])

        # # Adding model 'Product'
        # db.create_table(u'catalog_product', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Category'])),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        #     ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        #     ('description', self.gf('django.db.models.fields.TextField')(max_length=250)),
        #     ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        #     ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        # ))
        # db.send_create_signal(u'catalog', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Catalog'
        db.delete_table(u'catalog_catalog')

        # Deleting model 'Category'
        db.delete_table(u'catalog_category')

        # Deleting model 'Product'
        db.delete_table(u'catalog_product')


    models = {
        u'catalog.catalog': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Catalog'},
            # 'attach': ('esperancanordeste.fields.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'catalog.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'catalog.product': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['catalog']
