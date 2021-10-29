from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import RandomForm, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

from landing.forms import RandomForm
from .models import *

# Create your views here.


def home(request):

    

    context = {
        "login_form" : LoginForm(),
        "register_form" : RegisterForm(),
        "pins" : Pin.objects.all()
    }

    return render(request, 'home.html', context)

def about(request):

    context = {

        "title": "My second title"
    }

    return render(request, 'about.html', context)

def registerUser(request):
    if request.method== "GET":
        
        data = {'success': False, 
                'message':"Should be a POST request"}
        return JsonResponse(data)
    else:
        print(request.META)
        
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form. cleaned_data['name']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User()
            user.username = name
            user.age = age
            user.email = email
            user.set_password(password)
            user.save()

            login(request, user)
            mail_message = "Hello," + name+ ". Welcome to Our very own Pinterest Clone. Jibambe Msee."
            ##Send User Welcome Email
            send_mail(
                'Welcome to PinClone',
                mail_message,
                "admin@gmail.com",
                [email],
                fail_silently = False

            )

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        data = {'success': True, 
                'message':"Register Successful, Redirecting..."}
        return JsonResponse(data)
def loginUser(request):
    if request.method == 'GET':
        HttpResponse("Go home")
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request,user)
                context = {}

            

                return HttpResponseRedirect('/user/profile')
            else:
                messages.error(request, 'Login not successful')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

       
def profile(request):
    context = {}
    return render(request, 'profile.html', context)


def logout(request):

    logout(request)

    return HttpResponseRedirect('/')
