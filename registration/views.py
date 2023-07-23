from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('about')
    
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        repeat_password=request.POST['repeat_password']
        
        user_check=User.objects.filter(username=username).exists()
        if user_check==True:
            messages.error(request,"user already exist in database")
            return redirect('register')

        if password!=repeat_password:
            messages.error(request,"password not matched")
            return redirect('register')
        else:
            data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            data.save()
            messages.success(request,"account created")
        return redirect("login")
    return render(request,'SignUp.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('about')
    if request.method=='POST':
        user=request.POST['user']
        password=request.POST['password']
        user=authenticate(request,username=user,password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request,"successfull login ")
            return redirect('about')
        else:
            messages.error(request,"something went wrong")

    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    return redirect('index')