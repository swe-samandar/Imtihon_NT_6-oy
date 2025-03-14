from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserForm
from hashlib import sha256


class Main(View):
    def get(self, request):
        return render(request, 'register/index.html')


class Registration(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register/register.html', {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
        return render(request, 'register/register.html', {'form': form})


class Dashboard(View):
    def get(self, request):
        user = request.user
        return render(request, 'register/dashboard.html', {'user': user})
    

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')


class UserUpdate(View):
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        form = UserForm(instance=user)
        return render(request, 'register/user_update.html', {'form': form})
    
    def post(self, request):
        user = get_object_or_404(User, id=request.user.id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('dashboard')
        return render(request, 'register/user_update.html', {'form': form})