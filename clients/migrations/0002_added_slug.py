
from south.db import db
from django.db import models
from clients.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Client.slug'
        db.add_column('clients_client', 'slug', orm['clients.client:slug'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Client.slug'
        db.delete_column('clients_client', 'slug')
        
    
    
    models = {
        'clients.client': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['clients']
