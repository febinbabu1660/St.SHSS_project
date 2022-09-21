from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.login, name='teacher'),
    path('teacher', views.Teacher, name='teacher'),
    path('Teacher_index', views.Teacher, name='teacher_index'),

]
