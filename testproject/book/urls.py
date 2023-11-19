from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index, login_url='/login'), name='index'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    re_path(r'add$', views.book_add, name='book_add'),
    re_path(r'card/add(?P<slug>[\w-]+)/$', views.cars_add, name='card_add'),
    re_path(r'card/delete(?P<slug>[\w-]+)/$', views.card_delete, name='card_delete'),
    re_path(r'card/list/$', views.card_list, name='card_list'),

]
