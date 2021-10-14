from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html')


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            
            login(request, user)

            return redirect('/')

    return render(request, 'registration/register.html', {'form': form})   
    