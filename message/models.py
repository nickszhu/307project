from django.db import models

class Identification(models.Model):
    sender_ID = models.IntegerField()
    reciver_ID = models.IntegerField()

class Details(models.Model):
    message_body = models.CharField(max_length=100)
    date_sent = models.DateTimeField(auto_now=False, auto_now_add=False)
