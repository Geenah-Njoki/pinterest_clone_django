from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RandomForm

from landing.forms import RandomForm

# Create your views here.


def home(request):

    fruits=["mango", "apple", "melon", "avocado"] 


    context = {
        "title" : "My first title",
        "form" : RandomForm(),
        "first_name" : "Rey",
        "last_name" : "Mysterio",
        "second_name" : "Best",
        "third_name" : "Wrestler",
        "fruits" : fruits,
    }

    return render(request, 'home.html', context)

def about(request, title):

    context = {

        "titleFromHome" : title, 
        "title": "My second title"
    }

    return render(request, 'about.html', context)
