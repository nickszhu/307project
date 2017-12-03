from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators import csrf
from anyWares.models import Item, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from anyWares.forms import NewItemForm 
from django.template import Context   

def index(request):
    category_list = Category.objects.all()
    return render(request, 'anyWares/index.html', {'category_list': category_list})

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

        #if search_category != None:
        #    category = category_list.filter(category_name__icontains=search_category)
        #    if category.count() > 0: 
        #        item_list = item_list.get(category_ID=category)

        

    if not item_found:
        item_list = Item.objects.all() 
        
    page = request.GET.get('page', 1)

    paginator = Paginator(item_list, 9)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)   
    return render(request, 'anyWares/search.html', { 'items': items, 'item_found': item_found,'categsory_list': category_list })
    

def itemView(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'anyWares/itemView.html', {'item': item})

def createItem(request):
    category_list = Category.objects.all()
    #if request.method == 'POST':
        #form = NewItemForm(request.POST)
    return render(request, 'anyWares/createItem.html', {'category_list': category_list})

def account(request):
    return render(request, 'anyWares/account.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user= authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'anywares/signup.html', {'form': form})


def login(request):
    return render(request, 'anyWares/login.html')