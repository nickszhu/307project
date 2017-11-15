from django.http import HttpResponse

from django.shortcuts import render
from django.views.decorators import csrf

def index(request):
    return render(request, 'anyWares/index.html')


def search(request):  
    ctx ={}
    if request.POST:
        ctx['result'] = request.POST['search']
    return render(request, "anyWares/search.html", ctx)