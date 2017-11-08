from django.db import models

class Identification(models.Model):
    name = models.CharField(max_length=20)
    category_ID = models.IntegerField()
    owner_id = models.IntegerField()

class Details(models.Model):
    description = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.DurationField()
    picture = models.FileField()