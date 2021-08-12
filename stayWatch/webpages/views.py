from django.shortcuts import render
from .models import FeaturedCard,Stays
# Create your views here.

def index(request):
    return render(request, 'webpages_templates/index.html')

def home(request):
    featured = FeaturedCard.objects.all()
    s = set()
    for i in featured:
        s.add(Stays.objects.get(Name = i))
    
    data = {'featured':s}
    return render(request, 'webpages_templates/home.html',data)

def about(request):
    return render(request,'webpages_templates/about.html')


def explore(request):
    return render(request, 'webpages_templates/explore.html')



