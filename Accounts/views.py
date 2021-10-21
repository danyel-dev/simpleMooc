from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import RegisterForm, EditAccountForm, CommentForm
from Courses.models import subscribe, Course, Advert, Comment


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            
            login(request, user)
            return redirect('/')

    return render(request, 'registration/register.html', {'form': form})   
    

@login_required
def dashboard(request):
    registrations = subscribe.objects.order_by('-id').filter(user=request.user)
    return render(request, 'registration/dashboard.html', {'registrations': registrations})


@login_required
def edit_account(request):
    form = EditAccountForm(instance=request.user)

    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'registration/edit_account.html', {'form': form})


@login_required
def edit_password(request):
    form = PasswordChangeForm(user=request.user)
    
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'registration/edit_password.html', {'form': form})


@login_required
def course_adverts(request, slug):
    course = get_object_or_404(Course, slug_course=slug)
    Subscriber = get_object_or_404(subscribe, user=request.user, course=course)
    
    adverts = course.Adverts.all()

    if not Subscriber.is_approved():
        messages.error(request, 'Sua inscrição está pendente')
        return redirect('dashboard')
    
    return render(request, 'registration/course_adverts.html', {'course': course, 'adverts': adverts})


@login_required
def detail_advert(request, slug, id_advert):
    course = get_object_or_404(Course, slug_course=slug)
    Subscriber = get_object_or_404(subscribe, user=request.user, course=course)
    comment_form = CommentForm(request.POST or None)

    if not Subscriber.is_approved():
        messages.error(request, 'Sua inscrição está pendente')
        return redirect('dashboard')

    advert = get_object_or_404(Advert, pk=id_advert)

    if request.method == 'POST':
        comment = comment_form.save(commit=False)
        comment.advert = advert
        comment.user = request.user
        comment.save()
        
        comment_form = CommentForm()

    return render(request, 'registration/detail_advert.html', {'course': course, 'advert': advert, 'comment_form': comment_form})
