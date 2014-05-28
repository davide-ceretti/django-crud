from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Include all the urls for the following apps
    url(r'', include('apps.core.urls')),
    url(r'^items/', include('apps.items.urls')),

    # Basic django admin stuff
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
