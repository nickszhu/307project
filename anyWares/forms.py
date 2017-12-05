from django import forms
from anyWares.models import Item
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
                'name', 
                'category_ID', 
                'owner_ID', 
                'description', 
                'rental_price', 
                'start_date', 
                'end_date', 
                'address', 
                'address2', 
                'city', 
                'state', 
                'postal_code', 
                'country', 
                'image'
            ]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
