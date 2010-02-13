
from south.db import db
from django.db import models
from export.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Forwarder'
        db.create_table('export_forwarder', (
            ('id', orm['export.forwarder:id']),
            ('name', orm['export.forwarder:name']),
        ))
        db.send_create_signal('export', ['Forwarder'])
        
        # Adding field 'Record.forwarder'
        db.add_column('export_record', 'forwarder', orm['export.record:forwarder'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Forwarder'
        db.delete_table('export_forwarder')
        
        # Deleting field 'Record.forwarder'
        db.delete_column('export_record', 'forwarder_id')
        
    
    
    models = {
        'export.buyer': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'export.container': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'export.country': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'export.currency': {
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'export.forwarder': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'export.record': {
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Buyer']"}),
            'container': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['export.Container']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Country']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'file_no': ('django.db.models.fields.IntegerField', [], {}),
            'forwarder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Forwarder']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'order_confirm': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'payment_term': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'proforma_invoice': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'proforma_invoice_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shipment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Supplier']"})
        },
        'export.supplier': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['export']
