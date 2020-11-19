from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model  =  User
        fields = ['username','email','password1','password2']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title','body','topic']
        widget = {
            'tittle' : forms.TextInput(attrs={'size': 40, 'title': 'Your name','class':'form-control'}),
            'body' : forms.Textarea(attrs = {'class':'form-control'}),
            'topic' : forms.Select(attrs = {'class':'form-control'}),
        }