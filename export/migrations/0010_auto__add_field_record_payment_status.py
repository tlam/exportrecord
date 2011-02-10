# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Record.payment_status'
        db.add_column('export_record', 'payment_status', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Record.payment_status'
        db.delete_column('export_record', 'payment_status')


    models = {
        'clients.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'export.buyer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Buyer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'export.container': {
            'Meta': {'ordering': "['type', 'quantity']", 'object_name': 'Container'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'export.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'export.currency': {
            'Meta': {'ordering': "['code']", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'export.forwarder': {
            'Meta': {'object_name': 'Forwarder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'export.proformainvoicefile': {
            'Meta': {'object_name': 'ProformaInvoiceFile'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Record']"})
        },
        'export.record': {
            'Meta': {'ordering': "['file_no']", 'object_name': 'Record'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Buyer']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.Client']"}),
            'container': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['export.Container']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Country']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'file_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'forwarder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Forwarder']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order_confirm': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'payment_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'payment_term': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'proforma_invoice': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shipment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['suppliers.Supplier']", 'null': 'True'})
        },
        'suppliers.supplier': {
            'Meta': {'ordering': "['name']", 'object_name': 'Supplier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['export']
