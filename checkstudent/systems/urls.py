from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.check, name='index'),
    path('setting', views.setting, name='setting'),
    path('login', views.login, name='login'),
    path('student', views.view_data_student, name='student'),
    path('save', views.save_data_student, name='save_data'),
]