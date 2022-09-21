from django.shortcuts import render
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Teacher_Account
from django.contrib.auth import authenticate


def Teacher(request):
    return render(request, "teachers.html")


# def Home(request):
#     return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        name=request.POST['name']
        dob=request.POST['dob']
        place=request.POST['place']
        qualification=request.POST['qualification']
        mobile=request.POST['mobile']
        print(email,password,name, mobile,dob,place,qualification)
        if Teacher_Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        # elif Account.objects.filter(fname=fname).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            user=Teacher_Account.objects.create_user(email=email, password=password,name=name, mobile=mobile, dob=dob, place=place, qualification=qualification)
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
            return redirect('teacher_index')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('teacher')
    return render(request, '/')

def Teacher_index(request):
    return render(request, "teacher_index.html")
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
