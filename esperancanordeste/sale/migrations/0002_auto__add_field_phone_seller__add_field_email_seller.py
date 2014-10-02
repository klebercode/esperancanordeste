# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Phone.seller'
        db.add_column(u'sale_phone', 'seller',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sale.Seller']),
                      keep_default=False)

        # Removing M2M table for field phone on 'Seller'
        db.delete_table(db.shorten_name(u'sale_seller_phone'))

        # Removing M2M table for field email on 'Seller'
        db.delete_table(db.shorten_name(u'sale_seller_email'))

        # Adding field 'Email.seller'
        db.add_column(u'sale_email', 'seller',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['sale.Seller']),
                      keep_default=False)

        # # Adding model 'Estimate'
        db.create_table(u'sale_estimate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('segment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sale.Segment'])),
            ('enterprise', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('complement', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'sale', ['Estimate'])


    def backwards(self, orm):
        # Deleting field 'Phone.seller'
        db.delete_column(u'sale_phone', 'seller_id')

        # Adding M2M table for field phone on 'Seller'
        m2m_table_name = db.shorten_name(u'sale_seller_phone')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seller', models.ForeignKey(orm[u'sale.seller'], null=False)),
            ('phone', models.ForeignKey(orm[u'sale.phone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['seller_id', 'phone_id'])

        # Adding M2M table for field email on 'Seller'
        m2m_table_name = db.shorten_name(u'sale_seller_email')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seller', models.ForeignKey(orm[u'sale.seller'], null=False)),
            ('email', models.ForeignKey(orm[u'sale.email'], null=False))
        ))
        db.create_unique(m2m_table_name, ['seller_id', 'email_id'])

        # Deleting field 'Email.seller'
        db.delete_column(u'sale_email', 'seller_id')


    models = {
        u'sale.area': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Area'},
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sale.email': {
            'Meta': {'ordering': "['-default', 'address']", 'object_name': 'Email'},
            'address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'default': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sale.Seller']"})
        },
        u'sale.estimate': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Estimate'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'enterprise': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('tinymce.models.HTMLField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'segment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sale.Segment']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'sale.phone': {
            'Meta': {'ordering': "['-default']", 'object_name': 'Phone'},
            'default': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'operator': ('django.db.models.fields.IntegerField', [], {}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sale.Seller']"})
        },
        u'sale.segment': {
            'Meta': {'ordering': "['name']", 'object_name': 'Segment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'sale.seller': {
            'Meta': {'ordering': "['name', 'state']", 'object_name': 'Seller'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sale.Area']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'segment': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sale.Segment']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['sale']
