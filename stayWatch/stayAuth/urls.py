from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name = "login"),
    path('register',views.register,name = "register"),
    path('userLogout',views.userLogout,name = "userLogout"),
    path('dashboard',views.dashboard,name = "dashboard"),
]