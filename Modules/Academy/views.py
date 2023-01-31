from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contactForm(request):
    return render(request, 'contactForm.html')

def contact(request):
    if request.method == 'POST':
        subject = request.POST["subject"]
        message = request.POST["message"] + " / Email: " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        email_for = ["mtferreyra05@gmail.com"]
        send_mail(subject, message, email_from, email_for, fail_silently = False)
        return render(request, "successfulContact.html")
    return render(request, 'contactForm.html')
