from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import threading

from .models import Contact, Portfolio, Service


# 🏠 HOME PAGE
def home(request):
    return render(request, 'index.html')


# ⚙️ SERVICES PAGE
def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


# 🖼️ PORTFOLIO PAGE
def portfolio(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})


# 📩 CONTACT PAGE + FORM + EMAIL + NOTIFICATION
# Email function
def send_contact_email(subject, name, email, message):

    try:
        send_mail(
            f"New Contact: {subject}",
            f"""
New message received:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
            """,
            settings.EMAIL_HOST_USER,
            ['hanudigitalhub@gmail.com'],
            fail_silently=False,
        )

    except Exception as e:
        print("EMAIL ERROR:", e)


# CONTACT PAGE
def contact(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Background email
        threading.Thread(
            target=send_contact_email,
            args=(subject, name, email, message)
        ).start()

        return redirect('success')

    return render(request, 'contact.html')


def success(request):
    return render(request, 'success.html')