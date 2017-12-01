from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators import csrf
from anyWares.models import Item, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from anyWares.forms import SearchBarForm    

def index(request):
    catagory_list = Category.objects.all()
    return render(request, 'anyWares/index.html', {'catagory_list': catagory_list})

def search(request):
    catagory_list = Category.objects.all()  
    item_found = False
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        if search_query != None:
            item_list = Item.objects.filter(name__icontains=search_query) 
            if item_list.count() > 0:
                item_found = True

    if not item_found:
        item_list = Item.objects.all() 
        
    page = request.GET.get('page', 1)

    paginator = Paginator(item_list, 10)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)   
    return render(request, 'anyWares/search.html', { 'items': items, 'item_found': item_found,'catagsory_list': catagory_list })
    

def itemView(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'anyWares/itemView.html', {'item': item})

def createItem(request):
    return render(request, 'anyWares/createItem.html')

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