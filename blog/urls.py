from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('postcomment' , views.PostComment , name='PostComment'),
    path('',views.Bloghome ,name='Bloghome'),
    path('<str:slug>',views.blogpost , name='blogpost')
]
