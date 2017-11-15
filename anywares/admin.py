from django.contrib import admin

from .models import User_Profile, Category, Item, Item_Calandar, Rental, Rental_Calandar, Message

admin.site.register(User_Profile)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Item_Calandar)
admin.site.register(Rental)
admin.site.register(Rental_Calandar)
admin.site.register(Message)
