from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):

    if request.method =="POST":
        print('submitted REG')
        return redirect('register')
    else:
        return render(request,'accounts/dashboard.html')

def login(request):
    # checking the method
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            # loggin the user
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'User not found')
            return redirect('login')    
    else:    
      return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email has already taken')
                    return redirect('register')

                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                    username=username,email=email,password=password)
                    user.save()
                    # messages.success(request,'Your a successfully registered and can login now')
                    # return redirect('login')
                    auth.login(request,user)
                    messages.success(request,'You are now logged in')
                    return redirect('index')

        else: 
            messages.error(request,'Passwords do not matched')
            return redirect('register')    


    else:
        return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request,'You are loggout')
        return redirect('index')
    else:
      messages.error(request,"Don't try to be outsmart")
      return redirect('index')