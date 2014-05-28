from django.views.generic import (CreateView, ListView,
                                  UpdateView, DeleteView, DetailView,)
from django.core.urlresolvers import reverse

from apps.items.models import Item


class ToItemListMixin(object):
    """ A mixin that redirects you to item_list
    when get_success_url is called (usually on form.valid()). """
    def get_success_url(self):
        return reverse('item_list')


class ItemCreateView(ToItemListMixin, CreateView):
    model = Item


class ItemListView(ListView):
    model = Item


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(ToItemListMixin, UpdateView):
    model = Item


class ItemDeleteView(ToItemListMixin, DeleteView):
    model = Item
