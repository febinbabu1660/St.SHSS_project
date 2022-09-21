from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import authenticate


def Home(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        fname=request.POST['fname']
        lname=request.POST['lname']
        mobile=request.POST['mobile']
        print(email,password,fname,lname,mobile)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        # elif Account.objects.filter(fname=fname).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, fname=fname, lname=lname, mobile=mobile)
            user.save()
            messages.success(request, 'you are registered')
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email, password=password)
        print(email)
        print(password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            request.session['email']=email
            #request.session['fname']=user.fname
            # store user details in session
            # request.session['district']=user.district
            return redirect('student')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')

def student(request):
    return render(request, "student_index.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

