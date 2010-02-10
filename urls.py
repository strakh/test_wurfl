from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^test_wurfl/', include('test_wurfl.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'test_wurfl.views.root', name="hello"),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/strakh/Development/python/djcode/test_wurfl/site_media'}),
    
)
