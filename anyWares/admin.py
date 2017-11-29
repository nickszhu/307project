# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Profile, Category, Item, Item_Calandar, Rental, Rental_Calandar, Message

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Item_Calandar)
admin.site.register(Rental)
admin.site.register(Rental_Calandar)
admin.site.register(Message)
