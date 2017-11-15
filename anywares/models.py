from django.db import models
from django.contrib.auth.models import User

class User_Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    credit_card = models.CharField(max_length=20)
    card_experation_month = models.CharField(max_length=20)
    card_experation_year = models.CharField(max_length=20)
    billing_address = models.CharField(max_length=50)
    billing_city = models.CharField(max_length=20)
    billing_state = models.CharField(max_length=20)
    billing_postal_code = models.CharField(max_length=20)
    billing_country = models.CharField(max_length=20)
    lending_rating = models.DecimalField(max_digits=5, decimal_places=2)
    borrowing_rating = models.DecimalField(max_digits=5, decimal_places=2)
    DateStarted = models.DateTimeField(auto_now=False, auto_now_add=False)
    LastLogin = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.user)

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    picture = models.FileField()
    def __str__(self):
        return self.category_name

class Item(models.Model):
    name = models.CharField(max_length=20)
    category_ID = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner_ID = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_listed = models.DateTimeField(auto_now=False, auto_now_add=False)
    picture = models.FileField()
    def __str__(self):
        return self.name

class Item_Calandar(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_date = models.DateTimeField(auto_now=False, auto_now_add=False)

class Rental(models.Model):
    item_ID = models.ForeignKey(Item, on_delete=models.CASCADE)
    lender_ID = models.ForeignKey(User_Profile, null=True, related_name='lender')
    borrower_ID = models.ForeignKey(User_Profile, null=True, related_name='borrower')
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_state = models.CharField(max_length=20)
    lender_rating_of_borrower = models.DecimalField(max_digits=5, decimal_places=2)
    borrower_rating_of_lender = models.DecimalField(max_digits=5, decimal_places=2)

class Rental_Calandar(models.Model):
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now=False, auto_now_add=False)

class Message(models.Model):
    sender_ID = models.ForeignKey(User_Profile, null=True, related_name='sender')
    reciver_ID = models.ForeignKey(User_Profile, null=True, related_name='reciver')
    message_body = models.CharField(max_length=100)
    date_sent = models.DateTimeField(auto_now=False, auto_now_add=False)
