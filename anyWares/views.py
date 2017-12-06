import urllib
import urllib2
import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators import csrf
from anyWares.models import Item, Category, Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.template import Context   
from django.contrib.auth.models import User
from django.contrib import messages
import random, json, requests, collections
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from anyWares.forms import NewItemForm
from django.views.generic.edit import UpdateView
from django.forms.models import model_to_dict


def index(request):
    category_list = Category.objects.all()
    item_list = Item.objects.all()
    featured_items = []
    num_featured_items = range(1,3)
    for i in num_featured_items:
        random_index = random.randint(0, item_list.count() - 1)
        featured_items.append(item_list[random_index]) 
    return render(request, 'anyWares/index.html', {'category_list': category_list, 'featured_items': item_list})



def search(request):
    item_list = Item.objects.all()
    category_list = Category.objects.all()  
    search_args = {}
    item_found = False
    if request.method == 'GET':
        search_string = request.GET.get('search_box', None)
        search_category = request.GET.get('category_select', None)

        if search_string != None and search_category != None:
            if search_category == "Category":
                item_list = Item.objects.filter(name__icontains=search_string)
            else:
                category = category_list.filter(category_name__icontains=search_category)
                item_list = Item.objects.filter(name__icontains=search_string, category_ID=category) 
            if item_list.count() > 0:
                item_found = True

    if not item_found:
        item_list = Item.objects.all() 
        
    page = request.GET.get('page', 1)

    paginator = Paginator(item_list, 20)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)   
    return render(request, 'anyWares/search.html', { 'items': items, 'item_found': item_found,'categsory_list': category_list })

def myitems(request):
    item_found = False
    if request.method == 'POST':
        Item.objects.filter(id=request.POST.get('item_id')).delete()
        return redirect('myitems')
    current_user = request.user
    item_list = Item.objects.filter(owner_ID=current_user.profile)
    if item_list.count() > 0:
        item_found = True
        
    page = request.GET.get('page', 1)

    paginator = Paginator(item_list, 20)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)   
    return render(request, 'anyWares/myitems.html', { 'items': items, 'item_found': item_found }) 

def itemView(request):
    if request.method == 'GET':
        item_id = request.GET.get('item_id', None)
        item = Item.objects.get(pk=item_id)
    return render(request, 'anyWares/itemView.html', {'item': item})

def createItem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = json.load(response)
            ''' End reCAPTCHA validation '''

            if result['success']:
                new_item = form.save(commit=False)
                new_item.owner_ID = Profile.objects.get(user=request.user)
                new_item.save()
                new_item.refresh_from_db()
                return redirect(reverse('itemView') + '?item_id=' + str(new_item.pk))
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
    else:
        form = NewItemForm()
    return render(request, 'anyWares/createItem.html', {'form': form})

def account(request):
    if request.method == 'POST':
        current_user = request.user
        current_user.profile.first_name = request.POST.get('first_name')
        current_user.profile.last_name = request.POST.get('last_name')
        current_user.profile.address = request.POST.get('address')
        current_user.profile.address2 = request.POST.get('address2')
        current_user.profile.city = request.POST.get('city')
        current_user.profile.state = request.POST.get('state')
        current_user.profile.postal_code = request.POST.get('postal_code')
        current_user.profile.country = request.POST.get('country')
        current_user.profile.phone = request.POST.get('phone')
        current_user.profile.email = request.POST.get('email')
        current_user.save()
    return render(request, 'anyWares/account.html')

def about(request):
    return render(request, 'anyWares/about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = json.load(response)
            ''' End reCAPTCHA validation '''

            if result['success']:
                user = form.save()
                user.refresh_from_db()
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user= authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return render(request, 'anywares/signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'anywares/signup.html', {'form': form})

def edititem(request):
    if request.method == 'GET':
        item = Item.objects.get(id=request.GET.get('item_id'))
        form = NewItemForm(request.POST or None, instance=item)
    elif request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        item = Item.objects.get(pk=request.POST.get("item_id"))
        if form.is_valid():
            data = form.cleaned_data
            item.name = data['name']
            item.category_ID = data['category_ID']
            item.description = data['description']
            item.rental_price = data['rental_price']
            item.start_date = data['start_date']
            item.end_date = data['end_date']
            item.address = data['address']
            item.address2 = data['address2']
            item.city = data['city']
            item.state = data['state']
            item.postal_code = data['postal_code']
            item.country = data['country']
            item.save()
            item.refresh_from_db()
            return redirect(reverse('itemView') + '?item_id=' + str(item.pk))
    else:
        form = NewItemForm()
    return render(request, 'anyWares/edititem.html', {'form': form, 'item': item})

'''
class UpdateItem(UpdateView):
    model = Item
'''

def get_search_suggestions(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        items = Item.objects.filter(name__icontains = q)[:20]
        results = []
        for item in items:
            item_json = {}
            item_json['id'] = item.id
            item_json['label'] = item.name
            item_json['value'] = item.name
            results.append(item_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/'
    return HttpResponse(data, mimetype)

def delete_item(request):
    if request.method == 'POST':
        Item.objects.filter(id=request.POST.get('item_id')).delete()
    return redirect('myitems')
