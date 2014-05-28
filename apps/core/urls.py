from django.conf.urls.defaults import patterns, url

from apps.core.views import (IndexView, SecretView, AboutView)

urlpatterns = patterns('',
    # Static core pages
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^secret/$', SecretView.as_view(), name='secret'),
    url(r'^about/$', AboutView.as_view(), name='about'),

    # Login, Logout
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),

)