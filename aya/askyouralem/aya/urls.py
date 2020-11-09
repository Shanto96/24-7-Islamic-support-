from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginpage,name="login"),
    path('registration/',views.registration,name="registration"),
    path('home/',views.home,name="home"),
    path('nav/',views.nav,name="nav"),
    path('quran/',views.quran,name="quran"),
]