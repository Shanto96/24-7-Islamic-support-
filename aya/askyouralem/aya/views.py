
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def login(request):
    context = {}
    return render(request,'aya/login.html')