from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm,QuestionForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password = password)

        if user is not None:
            login(request,user)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'Alem':
                    return redirect('index')
            else:
             return redirect('home')
        else:
            messages.info(request,'Username or password did not mathced')

    context = {}
    return render(request,'aya/login.html')
def logoutUser(request):
    logout(request)
    return redirect('login')
def registration(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user )
            return redirect('login')


    context = {'form':form}
    return render(request,'aya/register.html',context)
def home(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'aya/index.html',context)

def nav(request):
    return render(request,'aya/navbar.html')

def quran(request):
    context = {}
    return render(request,'aya/Quran.html')
def index(request):
    context ={}
    return render(request,'aya/home.html')
def question(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'aya/question.html',context)
def test(request):
    return render(request,'aya/text.html')