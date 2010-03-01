from django.conf.urls.defaults import *
 
urlpatterns = patterns('suppliers.views',
    url(r'^$', 'index', name='index'),
    #url(r'^(?P<slug>[\w-]+)/$', 'detail', name='detail'),
)
