from django import forms
from anyWares.models import Item
from django.forms import ModelForm

class ImageUploadForm(forms.Form):
    image = forms.ImageField()