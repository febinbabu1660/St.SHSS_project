# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# import datetime
#
#
# # Create your models here.
#
# class MyAccountManager(BaseUserManager):
#     def create_user(self, fname, lname, email, mobile, password=None):
#         if not email:
#             raise ValueError('User must have an email address')
#
#         if not lname:
#             raise ValueError('User must have an username')
#
#         user = self.model(
#             email=self.normalize_email(email),
#                         lname=lname,
#
#                         mobile=mobile,
#                         fname=fname,
#
#
#
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     # def create_superuser(self, fname, email, lname, password, mobile=None):
#     #     user = self.create_user(
#     #         email=self.normalize_email(email),
#     #         fname=fname,
#     #         password=password,
#     #         lname=lname,
#     #         mobile=mobile,
#     #
#     #     )
#     #     user.is_admin = True
#     #     user.is_active = True
#     #     user.is_staff = True
#     #     user.is_superadmin = True
#     #     user.save(using=self._db)
#     #     return user
#
#
# class Account(AbstractBaseUser):
#
#     id = models.AutoField(primary_key=True)
#     fname = models.CharField(max_length=100, blank=True, null=True)
#     lname = models.CharField(max_length=100, blank=True, null=True)
#     email = models.EmailField(max_length=100, unique=True)
#     mobile = models.BigIntegerField(default=0)
#
#     # required
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superadmin = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['fname', 'lname', 'mobile']
#
#     objects = MyAccountManager()
#
#     # def full_name(self):
#     #     return f'{self.first_name} {self.last_name}'
#
#     def _str_(self):
#         return self.email
#
#
#     def has_module_perms(self, add_label):
#         return True


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, fname, lname, mobile, email, password=None, username=None):
        if not email:
            raise ValueError('User must have an email address')

        if not lname:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
                        lname=lname,
                        mobile=mobile,
                        fname=fname,
                        password=password,
                        username=username

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, password=None, username=None):
#         if not email:
#             raise ValueError('User must have an email address')
#
#
#
#         user = self.model(
#             email=self.normalize_email(email),
#
#                         password=password,
#             username=username
#
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

    def create_superuser(self, password, username, email):
            user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,

            )
            user.is_admin = True
            user.is_active = True
            user.is_staff = True
            user.is_superadmin = True
            user.save(using=self._db)
            return user



class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    username=models.CharField(max_length=100, unique=True)
    mobile = models.BigIntegerField(default=0)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'mobile']
    # REQUIRED_FIELDS = ['username', 'password']


    objects = MyAccountManager()

    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    def str(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True