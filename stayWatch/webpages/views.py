from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'webpages_templates/index.html')

def home(request):
    return render(request, 'webpages_templates/home.html')

def about(request):
    pass


def explore(request):
    return render(request, 'webpages_templates/explore.html')



