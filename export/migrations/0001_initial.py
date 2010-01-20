
from south.db import db
from django.db import models
from export.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Container'
        db.create_table('export_container', (
            ('id', orm['export.Container:id']),
            ('type', orm['export.Container:type']),
            ('quantity', orm['export.Container:quantity']),
        ))
        db.send_create_signal('export', ['Container'])
        
        # Adding model 'Supplier'
        db.create_table('export_supplier', (
            ('id', orm['export.Supplier:id']),
            ('name', orm['export.Supplier:name']),
        ))
        db.send_create_signal('export', ['Supplier'])
        
        # Adding model 'Country'
        db.create_table('export_country', (
            ('id', orm['export.Country:id']),
            ('name', orm['export.Country:name']),
        ))
        db.send_create_signal('export', ['Country'])
        
        # Adding model 'Record'
        db.create_table('export_record', (
            ('id', orm['export.Record:id']),
            ('date', orm['export.Record:date']),
            ('file_no', orm['export.Record:file_no']),
            ('supplier', orm['export.Record:supplier']),
            ('proforma_invoice', orm['export.Record:proforma_invoice']),
            ('order_confirm', orm['export.Record:order_confirm']),
            ('payment_term', orm['export.Record:payment_term']),
            ('currency', orm['export.Record:currency']),
            ('amount', orm['export.Record:amount']),
            ('country', orm['export.Record:country']),
            ('shipment_date', orm['export.Record:shipment_date']),
            ('buyer', orm['export.Record:buyer']),
            ('note', orm['export.Record:note']),
            ('proforma_invoice_file', orm['export.Record:proforma_invoice_file']),
        ))
        db.send_create_signal('export', ['Record'])
        
        # Adding model 'Buyer'
        db.create_table('export_buyer', (
            ('id', orm['export.Buyer:id']),
            ('name', orm['export.Buyer:name']),
        ))
        db.send_create_signal('export', ['Buyer'])
        
        # Adding model 'Currency'
        db.create_table('export_currency', (
            ('id', orm['export.Currency:id']),
            ('code', orm['export.Currency:code']),
            ('country', orm['export.Currency:country']),
        ))
        db.send_create_signal('export', ['Currency'])
        
        # Adding ManyToManyField 'Record.container'
        db.create_table('export_record_container', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('record', models.ForeignKey(orm.Record, null=False)),
            ('container', models.ForeignKey(orm.Container, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Container'
        db.delete_table('export_container')
        
        # Deleting model 'Supplier'
        db.delete_table('export_supplier')
        
        # Deleting model 'Country'
        db.delete_table('export_country')
        
        # Deleting model 'Record'
        db.delete_table('export_record')
        
        # Deleting model 'Buyer'
        db.delete_table('export_buyer')
        
        # Deleting model 'Currency'
        db.delete_table('export_currency')
        
        # Dropping ManyToManyField 'Record.container'
        db.delete_table('export_record_container')
        
    
    
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
        'export.record': {
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Buyer']"}),
            'container': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['export.Container']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Country']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['export.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'file_no': ('django.db.models.fields.IntegerField', [], {}),
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
