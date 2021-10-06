from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from Courses.models import Course 


def home(request):
    return render(request, 'core/home.html', {'home': 'home'})


def contact(request):
    return render(request, 'core/contact.html', {'contact': 'contact'})


def courses(request):
    courses = Course.objects.order_by('-id')
    return render(request, 'core/list_courses.html', {'courses': courses})


def detail_course(request, slug):
    course = get_object_or_404(Course, slug_course=slug)
    return render(request, 'core/detail_course.html', {'course': course})
