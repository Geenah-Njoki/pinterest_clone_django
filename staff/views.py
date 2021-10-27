from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import EmailForm
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from .forms import EmailForm
from landing.models import Pin, Board, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import *





# Create your views here.

def dashboard(request):

    context = {
        'users': User.objects.all(),
        'email_form': EmailForm()
    }

    return render(request, 'dashboard.html', context)

def sendEmail(request):
    if request.method== "GET":
        
        data = {'success': False, 
                'message':"Should be a POST request"}
        return JsonResponse(data)
    else:
        
        form = EmailForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['recipient']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']

            


            mail_message = "Hello," + name+ ", "+ message
                ##Send User Welcome Email
            send_mail(
                'Pinterest Age Request',
                mail_message,
                "admin@gmail.com",
                [email],
                fail_silently = False

            )

            data = {'success': True, 
                'message':"Mail sent successfully"}

            return JsonResponse(data)

def viewUsers(request):
    context = {
        'users' : User.objects.all()
    }

    return render(request, 'users.html', context)

def viewPins(request):
    context = {
        'pins' : Pin.objects.all()
    }

    return render(request, 'pins.html', context)

def viewBoards(request):
    context = {
        'boards' : Board.objects.all()
    }

    return render(request, 'boards.html', context)

def viewComments(request):
    context = {
        'comments' : Comment.objects.all()
    }

    return render(request, 'comments.html', context)


def userDetails(request, id):

    user = User.objects.get(pk = id)
    context = {
        'user': user
    }
    
    return render(request, 'user_details.html', context)
def deleteUser(request, id):

    user = User.objects.get(pk=id)
    user.delete()

    

    if request.is_ajax():

        data = {}
        return JsonResponse(data)

    else:
        return HttpResponseRedirect('/staff/users')

class CreateBoard(CreateView):
        model= Board
        fields = '__all__'
        success_url = '/staff/boards'
        template_name = 'board_form.html'


