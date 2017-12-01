from django import forms
from anyWares.models import Category

class SearchBarForm(forms.Form):
    #category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'))
    search = forms.CharField(label='', max_length=100)