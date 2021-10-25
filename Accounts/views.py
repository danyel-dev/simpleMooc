from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import RegisterForm, EditAccountForm, CommentForm
from Courses.models import subscribe, Course, Advert, Comment, Lesson

from .decorators import subscription_required


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
@subscription_required
def course_adverts(request, slug):
    course = request.course
    adverts = course.Adverts.all()

    return render(request, 'registration/course_adverts.html', {'course': course, 'adverts': adverts})


@login_required
@subscription_required
def detail_advert(request, slug, id_advert):
    course = request.course
    advert = get_object_or_404(Advert, pk=id_advert)
    
    comment_form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.advert = advert
            comment.user = request.user
            comment.save()
            
            messages.success(request, 'Seu comentário foi enviado com sucesso')
            comment_form = CommentForm()
    
            return redirect('detail-advert', slug, id_advert)

    return render(request, 'registration/detail_advert.html', {'course': course, 'advert': advert, 'comment_form': comment_form})


@login_required
@subscription_required
def lessons(request, slug):
    course = request.course
    return render(request, 'registration/lessons.html', {'course': course})


@login_required
@subscription_required
def detail_lesson(request, slug, id_lesson):
    course = request.course
    lesson = get_object_or_404(Lesson, pk=id_lesson)
    
    if not lesson.is_available():
        messages.error(request, 'Aula indisponível')
        return redirect('lessons', slug)

    return render(request, 'registration/detail_lesson.html', {'lesson': lesson, 'course': course})
