from django.shortcuts import render
from django.http import HttpResponse

from Courses.models import Course 


def home(request):
    return render(request, 'home.html', {'home': 'home'})


def contact(request):
    return render(request, 'contact.html', {'contact': 'contact'})


def courses(request):
    courses = Course.objects.order_by('-id')
    return render(request, 'courses.html', {'courses': courses})
