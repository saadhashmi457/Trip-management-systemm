from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponse



# Create your views here.
def signup_view(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        if password == cpassword:
            user=User.objects.create_user(username=username,email=email,password=password)
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Password not match")
    
    return render(request,"accounts/signup.html")

def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("invalid crediantials")
    

    return render(request,"accounts/login.html")

def logout_view(request):
    logout(request)
    
    return redirect('login')