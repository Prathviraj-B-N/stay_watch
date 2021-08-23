from django.db import models
from django.shortcuts import get_object_or_404, render
from .models import Stays
from django.template import Context
# Create your views here.

def index(request):
    return render(request, 'webpages_templates/index.html')

def home(request):
    featured = Stays.objects.filter(isFeatured = True)
    s = set()
    for i in featured:
        s.add(Stays.objects.get(name = i))
    
    data = {'featured':s}
    return render(request, 'webpages_templates/home.html',data)

def about(request):
    return render(request,'webpages_templates/about.html')


def explore(request):
    stays = Stays.objects.all()
    data = {'stays':stays}
    return render(request, 'webpages_templates/explore.html',data)

def stayDetails(request, id):
    stays = get_object_or_404(Stays,pk=id)
    data = {'stays':stays}
    return render(request, 'webpages_templates/stayDetails.html',data)



