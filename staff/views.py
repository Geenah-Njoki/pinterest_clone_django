from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import EmailForm
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from .forms import EmailForm




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


