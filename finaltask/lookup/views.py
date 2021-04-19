from django.shortcuts import render,HttpResponse,redirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request =request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username and password')
        else:
            messages.error(request, 'Invalid Username and password')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form':form}) 


from .forms import RegistrationForm
def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('/')