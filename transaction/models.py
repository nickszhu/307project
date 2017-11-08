from django.db import models

class Identification(models.Model):
    item_ID = models.IntegerField()
    lender_ID = models.IntegerField()
    borrower_ID = models.IntegerField()

class Details(models.Model):
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_state = models.CharField(max_length=20)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    lender_rating_of_borrower = models.DecimalField(max_digits=5, decimal_places=2)
    borrower_rating_of_lender = models.DecimalField(max_digits=5, decimal_places=2)
