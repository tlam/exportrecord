from django.conf.urls.defaults import include, patterns, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('export.urls', namespace='export'), name='records'),
    url(r'^clients/', include('clients.urls', namespace='clients'), name='clients'),
    url(r'^suppliers/', include('suppliers.urls', namespace='suppliers'), name='suppliers'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
