from . import views
from django.urls import path


urlpatterns = [
    # path('tlogin/', views.Tlogin, name='tlogin'),
    path('teacher_reg/', views.Teacher_reg, name='teacher_reg'),
    path('Teachers', views.Teachers, name='teachers'),
    path('TeachersHome', views.TeachersHome, name='TeachersHome'),
    path('Tdetail/', views.Tdetail, name='Tdetail'),
    path('Feedback/', views.Feedback, name='Feedback'),
    # path('viewmarks/', views.viewmarks, name='viewmarks'),


]
