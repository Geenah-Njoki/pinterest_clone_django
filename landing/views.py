from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    context = {
        "title" : "My first title"
    }

    return render(request, 'home.html', context)

def about(request, title):

    context = {

        "titleFromHome" : title, 
        "title": "My second title"
    }

    return render(request, 'about.html', context)
