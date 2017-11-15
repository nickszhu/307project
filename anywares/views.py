from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("This is the index page.")

def get_user_profile(request, username):
    return HttpResponse("You're looking at %s's profile." % username)

def item_details(request, item_id):
    return HttpResponse("You're looking at the item details of %s." % item_id)

