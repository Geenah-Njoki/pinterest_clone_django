from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RandomForm, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from landing.forms import RandomForm

# Create your views here.


def home(request):

    fruits=["mango", "apple", "melon", "avocado"] 


    context = {
        "title" : "My first title",
        "login_form" : LoginForm(),
        "register_form" : RegisterForm(),
        "first_name" : "Rey",
        "last_name" : "Mysterio",
        "second_name" : "Best",
        "third_name" : "Wrestler",
        "fruits" : fruits,
    }

    return render(request, 'home.html', context)

def about(request):

    context = {

        "title": "My second title"
    }

    return render(request, 'about.html', context)

def registerUser(request):
    if request.method== "GET":
        return HttpResponse("We don't want Get requests here")
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

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
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

            

                return render (request, 'profile.html', context)
            else:
                messages.error(request, 'Login not successful')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
