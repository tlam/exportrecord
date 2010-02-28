from django.conf.urls.defaults import *
 
urlpatterns = patterns('clients.views',
    url(r'^$', 'index', name='index'),
)
