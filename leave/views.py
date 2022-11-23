from django.shortcuts import render
from django.shortcuts import redirect
from .models import leaveModel

# Create your views here.


def leave(request):

    data=leaveModel.objects.filter(email=request.user.email)
    context = {
        'data': data
    }
    return render(request, 'leave/leave_view.html', context)

def leaveApply(request):
    if request.method == 'POST':
        print('1')
        name = request.POST['name']
        leaveDate = request.POST['date']
        leaveDiv = request.POST['session']
        leaveReason = request.POST['reason']
        leaveRecords = request.POST['proof']
        print(leaveDate)
        if leaveDiv=='FD':
            leaveDiv='AN, FN'
        leaveStatus = False
        email = request.user
        leaveModel.objects.create(name=name,email=email, leaveDate=leaveDate, leaveDiv=leaveDiv, leaveReason=leaveReason, leaveStatus=leaveStatus, leaveRecords=leaveRecords)
        return redirect('leave')


    return render(request, 'Leave/leave.html')