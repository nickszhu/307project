from django.db import models

class Identification(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Location(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

class BillingInfo(models.Model):
    credit_card = models.CharField(max_length=20)
    card_experation_month = models.CharField(max_length=20)
    card_experation_year = models.CharField(max_length=20)
    billing_address = models.CharField(max_length=50)
    billing_city = models.CharField(max_length=20)
    billing_state = models.CharField(max_length=20)
    billing_postal_code = models.CharField(max_length=20)
    billing_country = models.CharField(max_length=20)

class ProfileInfo(models.Model):
    lending_rating = models.DecimalField(max_digits=5, decimal_places=2)
    borrowing_rating = models.DecimalField(max_digits=5, decimal_places=2)
    DateStarted = models.DateTimeField(auto_now=False, auto_now_add=False)
    LastLogin = models.DateTimeField(auto_now=False, auto_now_add=False)


