from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def loginUser(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username = username, password= password)
        
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
            return redirect("loginUser")
    
    return render(request,'user/login.html')

def registerUser(request):
    return render(request,'user/register.html')
