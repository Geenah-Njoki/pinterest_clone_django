from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import EmailForm
from django.contrib import messages
from django.core.mail import send_mail




# Create your views here.

def dashboard(request):

    context = {
        'users': User.objects.all()
    }

    return render(request, 'dashboard.html', context)

def sendEmail(request):
    if request.method== "GET":
        
        data = {'success': False, 
                'message':"Should be a POST request"}
        return JsonResponse(data)
    else:
        print(request.META)
        
        form = EmailForm(request.POST)

        if form.is_valid():
            age = form.cleaned_data['age']


        sendEmail(request, user)
        mail_message = "Hello," + name+ ". Welcome to Our very own Pinterest Clone. Jibambe Msee."
            ##Send User Welcome Email
        sendEmail(
            'Welcome to PinClone',
            mail_message,
            "admin@gmail.com",
            [email],
            fail_silently = False

            )

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER')
