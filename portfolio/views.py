import imp
from django.shortcuts import render

# Create your views here.
from .models import Image
from django.core.mail import EmailMessage


def index(request):
    images  = Image.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # print(name + '\n' + email + "\n" + subject + "\n" + message) 
        email_message = EmailMessage(
            subject = name + " : "+ subject,
            body=message,
            to=['hwauie23@gmail.com'],
            headers = {"Reply to " : email},
        )
        email_message.send()
    context = {

        'images': images
    }
    return render(request , 'index.html', context)