from django.http import HttpResponse

from django.shortcuts import render
from django.views.decorators import csrf
from anyWares.models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'anyWares/index.html')


def search(request):  
    item_list = Item.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(item_list, 10)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'anyWares/search.html', { 'items': items })
    

#def itemView(request):
 #   ctx ={}
  #  if request.POST:
 #       ctx['result'] = request.POST['search']
 #   return render(request, "anyWares/search.html", ctx)