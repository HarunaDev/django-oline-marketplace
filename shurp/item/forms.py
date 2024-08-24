# create form to handle adding items
from django import forms

from .models import Item

# form to allow users add items
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        