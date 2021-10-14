from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth

from .forms import RegisterForm


def dashboard(request):
    return render(request, 'registration/dashboard.html')


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user = auth.authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            
            auth.login(request, user)

            return redirect('/')

    return render(request, 'registration/register.html', {'form': form})   
    