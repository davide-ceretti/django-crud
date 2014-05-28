from django import forms

from apps.items.models import Item


class ItemForm(forms.ModelForm):
    """ A basic form used to create or edit an Item """
    class Meta:
        model = Item
        fields = ('content',)
