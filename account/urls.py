from django.urls import path 
from  . import views
from django.contrib.auth.forms import UserCreationForm
urlpatterns = [
    path('singup/',views.singup,name='singup'),
    path('logout/',views.logoutaccount,name='logoutaccount'),
    path('login/',views.loginaccount,name='loginaccount'),
 
]
