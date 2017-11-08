from django.db import models

class Identification(models.Model):
    category_name = models.CharField(max_length=20)

class Details(models.Model):
    description = models.CharField(max_length=100)
    picture = models.FileField()
