from django.http import request
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'stayAuth/login.html')

def register(request):
    pass

def userLogout(request):
    pass

def dashboard(request):
    pass