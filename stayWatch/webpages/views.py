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
    #filter search
    city_search_list = Stays.objects.values_list('city',flat=True).distinct()
    cost_search_list = Stays.objects.values_list('cost',flat=True).distinct()
    rating_search_list = Stays.objects.values_list('rating',flat=True).distinct()
    pincode_search_list = Stays.objects.values_list('pincode',flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            stays = stays.filter(city__icontains = keyword) | stays.filter(name__icontains = keyword)
            

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            stays = stays.filter(city__exact = city)

    if 'pincode' in request.GET:
        pincode = request.GET['pincode']
        if pincode:
            stays = stays.filter(city__exact = pincode)

    if 'rating' in request.GET:
        rating = request.GET['rating']
        if rating:
            stays = stays.filter(city__exact = rating)

    if 'cost' in request.GET:
        cost = request.GET['cost']
        if cost:
            stays = stays.filter(city__exact = cost)
    
    
    data = {
        'stays':stays,
        'city_search_list':city_search_list,
        'cost_search_list':cost_search_list,
        'rating_search_list':rating_search_list,
        'pincode_search_list':pincode_search_list,
        }

    return render(request, 'webpages_templates/explore.html',data)

def stayDetails(request, id):
    stays = get_object_or_404(Stays,pk=id)
    data = {'stays':stays}
    return render(request, 'webpages_templates/stayDetails.html',data)



