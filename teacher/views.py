from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Teacher, Tdetails
from django.contrib.auth import authenticate
from Schoolapp.models import Account


def Teachers(request):
    return render(request, "Teacher/teachers.html")

def TeachersHome(request):
    return render(request, "Teacher/teacher_index.html")
# def Home(request):
#     return render(request, "index.html")

def Teacher_reg(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        # dob=request.POST['dob']
        place=request.POST['place']
        # qualification=request.POST['qualification']
        mobile = request.POST['mobile']
        username = email.split('@')[0]
        # print(email,password,name, mobile,dob,place,qualification)
        teach = Teacher.objects.filter(email=email).exists()
        if teach:
            messages.error(request, 'email already exists')
            return render('teachers')
        # elif Account.objects.filter(fname=fname).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            teach = Teacher(email=email, password=password, username=username, mobile=mobile,
                            fname=fname, lname=lname, place=place)
            teach.save()
            messages.success(request, 'you are registered')
            return redirect('teachers')
    return render(request, 'Teacher/teacher_index.html')

#
# def Tlogin(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email, password=password)
#         print(email)
#         print(password)
#         print(user)
#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'you are logged in')
#             request.session['email'] = email
#             # request.session['fname']=user.fname
#             # store user details in session
#             # request.session['district']=user.district
#             return redirect('teacher_index')
#         else:
#             messages.error(request, 'invalid login credentials')
#             return redirect('teachers')
#     return render(request, 'Teacher/teacher_index.html')


def Teacher_index(request):
    return render(request, "Teacher/teacher_index.html")

#
# def Tdetail(request):
#     return render(request, "Teacher/teacher_details.html")

from Schoolapp.models import Course
def Tdetail(request):
    if request.method == 'POST':
        user=request.user
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        hname = request.POST.get('hname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        caste = request.POST.get('Caste')
        qualification = request.POST.get('qualification')
        resume = request.POST.get("resume")
        timage = request.POST.get("timage")
        subject = request.POST.get("subject")
        place = request.POST.get("place")
        mobile = request.POST.get("mobile")
        id = request.POST.get("Course_name")
        C=Course.objects.get(id=id)

        suser = Tdetails(email=user,fname=fname, lname=lname, hname=hname, dob=dob, gender=gender, caste=caste, qualification=qualification, resume=resume, timage=timage, subject=subject, place=place, mobile=mobile,Course_name=C)
        suser.save()
        curse=Course.objects.all()
        return render(request, 'Teacher/teacher_details.html',{'curse':curse})
    else:
        curse = Course.objects.all()
        return render(request, 'Teacher/teacher_details.html',{'curse':curse})


#
# def viewmarks(request):
#     return render(request, "Teacher/viewmark.html")


def Feedback(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fdback = request.POST.get('fdback')

        # check if user already exists
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'feedback sent')
            return redirect('Feedback')
        else:
            message = fdback

            send_mail(
                'Feedback',
                message,
                'febinbabu2000@gmail.com',
                [email],
                fail_silently=False,
            )

            return redirect('/register/?command=verification&email=' + email)

    return render(request, "Teacher/feedback.html")
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
