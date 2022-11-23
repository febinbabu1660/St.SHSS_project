from django.shortcuts import render

from Schoolapp.models import Subjects


# Create your views here.
from  Schoolapp.models import Sdetails
def Enter_mark(request):
    a=Subjects.objects.filter(email__id=request.user.id).values_list('Subject_name') #subname
    # b=Sdetails.objects.filter(email__role="Student", Course_name__Subject_name=a)
    c = Sdetails.objects.filter(email__role="Student", Course_name=list((Subjects.objects.filter(Subject_name=a)).values_list('Course_name')))
    # c=Subjects.objects.filter()

    print(a)
    print(c)
    return render(request, "Teacher/Enter_mark.html")

