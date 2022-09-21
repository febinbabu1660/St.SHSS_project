from . import views
from django.urls import path


urlpatterns = [
    path('',views.Home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('student/', views.student, name='student'),
    path('logout', views.logout, name='logout'),

]
