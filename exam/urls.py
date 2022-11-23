from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Enter_mark, name='Enter_mark'),

    ]