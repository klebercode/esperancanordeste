# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # # Adding field 'Catalog.attach'
        # db.add_column(u'catalog_catalog', 'attach',
        #               self.gf('esperancanordeste.fields.ContentTypeRestrictedFileField')(default=0, max_length=100),
        #               keep_default=False)

        # Adding field 'Category.image'
        db.add_column(u'catalog_category', 'image',
                      self.gf('sorl.thumbnail.fields.ImageField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Catalog.attach'
        db.delete_column(u'catalog_catalog', 'attach')

        # Deleting field 'Category.image'
        db.delete_column(u'catalog_category', 'image')


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
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
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
