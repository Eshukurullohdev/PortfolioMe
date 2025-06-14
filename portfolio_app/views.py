from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

from django.core.mail import send_mail

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject=f"New Contact from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email=email,
            recipient_list=['your_email@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'thanks.html')

    return render(request, 'contact.html')
