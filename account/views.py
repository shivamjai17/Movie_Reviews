from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import  login,logout,authenticate
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def singup(request):
    if request.method =='GET':
        return render(request,'singup.html',{'form':UserCreateForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:

                user=User.objects.create_user(
                request.POST['username'],
                password=request.POST['password1']
                )
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'singup.html',{'form':UserCreateForm,'error':'Username already exit chose new username'})    
        else:
            return redirect(request,'singup.html',{'form':UserCreateForm,'error':'Password do not match'})
        
@login_required
def logoutaccount(request):
    logout(request)
    return redirect('home')        
def loginaccount(request):
    if request.method=='GET':
        return render(request,'loginaccount.html',{'form':AuthenticationForm})
    else:
        user=authenticate(request,
        username=request.POST.get('username'),
        password=request.POST.get('password')              
                          )
        if user is None:
            return redirect(request,'loginaccount.html',{'form':AuthenticationForm(),'error':"username and password do not match"})
        else:
            login(request,user)
            return redirect(reverse('home'))
  