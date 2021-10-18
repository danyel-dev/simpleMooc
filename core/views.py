from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Courses.models import Course, subscribe 
from .forms import ContactCourse


def home(request):
    return render(request, 'core/home.html', {'home': 'home'})


def contact(request):
    return render(request, 'core/contact.html', {'contact': 'contact'})


def courses(request):
    courses = Course.objects.order_by('-id')
    return render(request, 'core/list_courses.html', {'courses': courses})


def detail_course(request, slug):
    course = get_object_or_404(Course, slug_course=slug)
    form = ContactCourse(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form = ContactCourse()

    return render(request, 'core/detail_course.html', {
        'course': course,
        'form': form,
    })


@login_required
def subscribe_course(request, slug):
    course = get_object_or_404(Course, slug_course=slug)
    Subscribe, create = subscribe.objects.get_or_create(user=request.user, course=course)

    if create:
        messages.success(request, 'Inscrição realizada com sucesso!')
        # Subscribe.active()
        # Subscribe.save()
    else:
        messages.error(request, 'Você já está inscrito nesse curso')

    return redirect('dashboard')


@login_required
def unsubscribe_course(request, slug):
    course = get_object_or_404(Course, slug_course=slug)
    Subscribe = get_object_or_404(subscribe, user=request.user, course=course)

    cancel = request.GET.get('cancel')

    if cancel:
        Subscribe.delete()
        return redirect('dashboard')

    return render(request, 'core/unsubscribe_course.html', {'course': course})
