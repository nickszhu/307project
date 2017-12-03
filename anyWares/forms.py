from django import forms
from anyWares.models import Category

class NewItemForm(forms.Form):
    item_name = forms.CharField(label='Item name', max_length=100)
