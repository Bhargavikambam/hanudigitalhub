from django.shortcuts import render, redirect
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


# 📩 CONTACT PAGE + FORM SAVE
def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
            subject=subject
        )

        return redirect('contact')

    return render(request, 'contact.html')