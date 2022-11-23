from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account, Sdetails, Course, class_Biomaths, class_Commerce, class_HomeScience
from django.contrib.auth import authenticate

# email verification import files
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail


def Home(request):
    return render(request, "index/index.html")


def About(request):
    return render(request, "index/about.html")


# def Courses(request):
#     return render(request, "courses.html")


def Pscience(request):
    return render(request, "Courses/pureScience.html")


def HScience(request):
    return render(request, "Courses/homeScience.html")


def Commerece(request):
    return render(request, "Courses/commerce.html")


def Humanities(request):
    return render(request, "Courses/Humanities.html")


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        role = request.POST['role']
        username = email.split('@')[0]
        print(email, password, fname, lname, mobile)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        # elif Account.objects.filter(fname=fname).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            user = Account.objects.create_user(username=username, email=email, password=password, fname=fname,
                                               lname=lname, mobile=mobile,role=role)
            user.save()
            messages.success(request, 'Thank you for registering with us.')
            messages.success(request, 'Please verify your email for login!')

            current_site = get_current_site(request)
            message = render_to_string('index/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'febinbabu2000@gmail.com',
                [email],
                fail_silently=False,
            )

            return redirect('/register/?command=verification&email=' + email)
            # return redirect('register')
    return render(request, 'index/index.html')


def Sdetail(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        hname = request.POST.get('hname')
        email = request.session['email']
        email_id = Account.objects.get(email=email)
        father = request.POST.get('father')
        occupation = request.POST.get('occupation')
        pmobile = request.POST.get('pmobile')
        dob = request.POST.get('dob')
        caste = request.POST.get('Caste')
        pschool = request.POST.get('pschool')
        mark = request.POST.get('mark')
        Stream = request.POST.get('Stream')
        slanguage = request.POST.get('slanguage')
        gender = request.POST.get('gender')
        gname = request.POST.get('gname')
        gmobile = request.POST.get('gmobile')
        # print('hello')
        suser = Sdetails(fname=fname, lname=lname, hname=hname, email=email, father=father, occupation=occupation, pmobile=pmobile,
                         dob=dob, caste=caste, pschool=pschool, mark=mark, Stream=Stream, slanguage=slanguage,
                         gender=gender, gname=gname, gmobile=gmobile)
        suser.save()

        if Stream == 'Commerce':
            commerce=class_Commerce(Student_name=fname, Student_email=email,Student_mob=pmobile)
            commerce.save()
        if Stream == 'Home Science':
            hscience=class_HomeScience(Student_name=fname, Student_email=email,Student_mob=pmobile)
            hscience.save()
        if Stream == 'Bio Science':
            bscience=class_Biomaths(Student_name=fname, Student_email=email,Student_mob=pmobile)
            bscience.save()
        messages.success(request, 'Your Details has been successfully uploaded..!!')
        return redirect('/')
    stream = Course.objects.all()
    return render(request, 'Student/Sdetails.html', {'stream': stream})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        print(email)
        print(password)
        print(user)
        if user is not None and user.is_student:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            request.session['email'] = email
            # request.session['fname']=user.fname
            # store user details in session
            # request.session['district']=user.district
            print(user.role)
            print("1")
            if user.role=="Student":
                print("3")
                return redirect('student')
            elif user.role=="Teacher":
                print("6")
                return redirect('TeachersHome')
            else:
                pass


        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'index/index.html')


def tchrlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        print(email)
        print(password)
        print(user)
        if user is not None and user.is_teacher:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            request.session['email'] = email
            # request.session['fname']=user.fname
            # store user details in session
            # request.session['district']=user.district
            return redirect('teacher')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('tchrlogin')
    return render(request, 'index/index.html')


# def login(request):
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
#             return redirect('student')
#         else:
#             messages.error(request, 'invalid login credentials')
#             return redirect('login')
#     return render(request, 'index.html')


def student(request):
    return render(request, "Student/student_index.html")


def Sdisplay(request):
    email = request.session['email']
    content = {
        'Stddetails': Sdetails.objects.all(),
        'email': email
    }
    return render(request, "Student/Sdetails_display.html", content)


def Courses(request):
    obj = Course.objects.all()
    return render(request, "Courses/courses.html", {'result': obj})


def logout(request):
    auth.logout(request)
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('register')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')
