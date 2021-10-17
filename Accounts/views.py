from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import RegisterForm, EditAccountForm
from Courses.models import subscribe


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
def course_user(request, slug):
    return render(request, 'registration/course-user.html')
