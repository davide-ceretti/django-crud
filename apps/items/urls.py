from django.conf.urls.defaults import patterns, url

from apps.items.views import (
    ItemCreateView, ItemListView, ItemDeleteView, ItemUpdateView,
    ItemDetailView,)


urlpatterns = patterns('',
    url(r'^add/$', ItemCreateView.as_view(), name='item_create'),
    url(r'^$', ItemListView.as_view(), name='item_list'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='item_update'),
    url(r'^(?P<pk>\d+)/delete/$', ItemDeleteView.as_view(), name='item_delete'),
)
