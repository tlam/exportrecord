from django.conf.urls.defaults import *
 
urlpatterns = patterns('export.views',
    url(r'^$', 'index', name='home'),
    url(r'^login/$', 'home_login', name='home-login'),
)
