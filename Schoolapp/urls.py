from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('tchrlogin/', views.tchrlogin, name='tchrlogin'),

    path('about/', views.About, name='about'),
    path('courses/', views.Courses, name='courses'),
    path('student/', views.student, name='student'),
    path('Sdetails/', views.Sdetail, name='Sdetails'),
    path('Sdisplay/', views.Sdisplay, name='Sdisplay'),
    path('Pscience/', views.Pscience, name='Pscience'),
    path('HScience/', views.HScience, name='HScience'),
    path('Commerece/', views.Commerece, name='Commerece'),
    path('Humanities/', views.Humanities, name='Humanities'),

    path('logout', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]
