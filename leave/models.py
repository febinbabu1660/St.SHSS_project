from django.db import models

# Create your models here.
from django.db import models




# Create your models here.


class leaveModel(models.Model):
    leave_choices = (
        ('FN', 'FN'),
        ('AN', 'AN'),
        ('FD', 'FD'),
        ('None', 'None'),
    )
    leaveId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=30)
    leaveDate = models.DateField()
    leaveDiv = models.CharField(max_length=10)
    leaveReason = models.CharField(max_length=50)
    leaveStatus = models.BooleanField('Approved', default=False)
    leaveRecords = models.FileField(upload_to="media/leave/")


    def __str__(self):
        return self.email

