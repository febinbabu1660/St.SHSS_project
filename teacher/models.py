from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime

from  Schoolapp.models import Account

# Create your models here.

# class MyAccountManager(BaseUserManager):
#     def create_user(self, name, mobile, email, password=None, username=None, dob=None, place=None, qualification=None):
#         if not email:
#             raise ValueError('User must have an email address')
#
#         if not name:
#             raise ValueError('User must have an username')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             name=name,
#             mobile=mobile,
#             fname=fname,
#             password=password,
#             username=username,
#             dob=dob,
#             place=place,
#             qualification=qualification,
#
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#
from Schoolapp.models import Course


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    mobile = models.BigIntegerField(default=0)
    password = models.CharField(max_length=200, null=True)
    # required
    # dob = models.DateTimeField(auto_now_add=True)
    # place = models.CharField(max_length=100, blank=True, null=True)
    # qualification = models.CharField(max_length=100, blank=True, null=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['fname', 'lname', 'mobile', 'dob', 'place', 'qualification']
    # REQUIRED_FIELDS = ['username', 'password']

    # objects = MyAccountManager()

    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fname

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    #
    # def has_module_perms(self, add_label):
    #     return True


class Tdetails(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    hname = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    Course_name = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    mobile = models.BigIntegerField(default=0)
    dob = models.DateTimeField(auto_now_add=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    resume = models.FileField(upload_to="media/resume/")
    timage = models.FileField(upload_to="media/T_image/")

    def __str__(self):
        return self.fname
