from django import forms
from anyWares.models import Category

class NewItemForm(forms.Form):
    item_name = forms.CharField(label='Item name', max_length=100)
    item_category = forms.ModelChoiceField(queryset=Category.objects.all())
    item_price = forms.IntegerField(max_value=None, min_value=0)
    item_availability_start = forms.DateField()
    item_availability_end = forms.DateField()
    item_image = forms.ImageField()
    item_pickup_location = forms.CharField(max_length=100)