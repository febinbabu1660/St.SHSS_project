from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime


# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, fname, lname, mobile, email, role, password=None, username=None):
        if not email:
            raise ValueError('User must have an email address')

        if not lname:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            lname=lname,
            mobile=mobile,
            fname=fname,
            role=role,
            password=password,
            username=username

        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, password, username, email):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = False
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    mobile = models.BigIntegerField(default=0)
    role = models.CharField(default=0,max_length=20)

    # required
    date_joined = models.DateTimeField(auto_now_add=False,null=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'mobile']
    # REQUIRED_FIELDS = ['username', 'password']

    objects = MyAccountManager()

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    Course_name = models.CharField(max_length=100, blank=True, null=True)
    Course_img = models.ImageField(upload_to='course/subject', null=True)
    Description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Course_name



class Sdetails(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    hname = models.CharField(max_length=100, blank=True, null=True)
    father = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    pmobile = models.CharField(default=0,max_length=200)
    email = models.EmailField(default=0,blank=True,null=True)
    # username = models.CharField(max_length=100, unique=True)
    # mobile = models.BigIntegerField(default=0)
    dob = models.DateField(auto_now_add=False)
    caste = models.CharField(max_length=100, blank=True, null=True)
    # nationality = models.CharField(max_length=50, blank=True, null=True)
    pschool = models.CharField(max_length=100, blank=True, null=True)
    mark = models.CharField(blank=True, null=True,max_length=200)
    # Course_name = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True)
    Stream = models.CharField(max_length=100, blank=True, null=True)
    slanguage = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    gname = models.CharField(max_length=100, blank=True, null=True)
    gmobile = models.CharField(blank=True, null=True,max_length=200)

    # required
    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now_add=False)
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # is_superadmin = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.fname





class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    Subject_name = models.CharField(max_length=100, blank=True, null=True)
    Course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    email = models.ForeignKey(Account, on_delete=models.CASCADE)

    # Description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Subject_name




class SLanguage(models.Model):
    id = models.AutoField(primary_key=True)
    SLanguage_name = models.CharField(max_length=100, blank=True, null=True)
    Course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    # Description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.SLanguage_name



class class_Biomaths(models.Model):
    Student_name = models.CharField(max_length=100,blank=True, null=True)
    Student_email = models.EmailField(max_length=100, unique=True)
    Student_mob = models.BigIntegerField(default=0)

    def __str__(self):
        return self.Student_name


class class_Commerce(models.Model):
    Student_name = models.CharField(max_length=100, blank=True, null=True)
    Student_email = models.EmailField(max_length=100, unique=True)
    Student_mob = models.BigIntegerField(default=0)

    def __str__(self):
        return self.Student_name


class class_Humanities(models.Model):
    Student_name = models.CharField(max_length=100, blank=True, null=True)
    Student_email = models.EmailField(max_length=100, unique=True)
    Student_mob = models.BigIntegerField(default=0)

    def __str__(self):
        return self.Student_name


class class_HomeScience(models.Model):
    Student_name = models.CharField(max_length=100, blank=True, null=True)
    Student_email = models.EmailField(max_length=100, unique=True)
    Student_mob = models.BigIntegerField(default=0)

    def __str__(self):
        return self.Student_name



