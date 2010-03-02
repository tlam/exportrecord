
from south.db import db
from django.db import models
from suppliers.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Supplier'
        db.create_table('suppliers_supplier', (
            ('id', orm['suppliers.Supplier:id']),
            ('name', orm['suppliers.Supplier:name']),
            ('slug', orm['suppliers.Supplier:slug']),
        ))
        db.send_create_signal('suppliers', ['Supplier'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Supplier'
        db.delete_table('suppliers_supplier')
        
    
    
    models = {
        'suppliers.supplier': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['suppliers']
