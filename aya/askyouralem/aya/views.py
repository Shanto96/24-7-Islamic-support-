from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.


def loginpage(request):
    context = {}
    return render(request,'aya/login.html')
def registration(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ )
            return redirect('login')


    context = {'form':form}
    return render(request,'aya/register.html',context)
def home(request):
    context = {}
    return render(request,'aya/home.html')
