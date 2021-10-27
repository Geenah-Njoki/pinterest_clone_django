"""pinterest_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from staff import views


urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('user/sendEmail', views.sendEmail, name="user.sendEmail"),
    path('users', viewUsers, name='users'),
    path('users/<int:id>', userDetails, name="user.details"),
    path('users/delete/<int:id>', deleteUser, name="user.delete"),
    path('pins', viewPins, name='pins'),
    path('boards', viewBoards, name='boards'),
    path('comments', viewComments, name='comments'),
    path('boards/create', CreateBoard.as_view(), name="create.board")

    

    
]
