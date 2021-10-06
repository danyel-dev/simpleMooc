from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from Courses.models import Course 


def home(request):
    return render(request, 'home.html', {'home': 'home'})


def contact(request):
    return render(request, 'contact.html', {'contact': 'contact'})


def courses(request):
    courses = Course.objects.order_by('-id')
    return render(request, 'courses.html', {'courses': courses})


def course_detail(request, id_course):
    course = get_object_or_404(Course, id=id_course)
    return render(request, 'course_detail.html', {'course': course})
