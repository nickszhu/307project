from django import forms
from anyWares.models import Item
from django.forms import ModelForm

class NewItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category_ID', 'owner_ID', 'description', 'rating']
