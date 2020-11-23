from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.core.validators import RegexValidator
from django.db.models import  Q
from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

import random
import os



class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    CHOICES = (
        ("WOMEN_ENTREPRENEUR", 'Women Entrepreneur'),
        ("INFLUENCER", 'Influencer'),
        ("BUYER", 'Buyer'),
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
    phone = models.CharField('Phone', validators=[phone_regex], max_length=10, unique=True, null=True)
    REQUIRED_FIELD = ['username', 'phone']

    objects = UserManager()


class PhoneOTP(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    count = models.IntegerField(default=0, help_text='Number of otp_sent')
    validated = models.BooleanField(default=False,
                                    help_text='If it is true, that means user have validate otp correctly in second API')
    otp_session_id = models.CharField(max_length=120, null=True, default="")
    username = models.CharField(max_length=20, blank=True, null=True, default=None)
    email = models.CharField(max_length=50, null=True, blank=True, default=None)
    password = models.CharField(max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)

class User(AbstractUser):
    CHOICES = (
        ("WOMEN_ENTREPRENEUR", 'Women Entrepreneur'),
        ("INFLUENCER", 'Influencer'),
        ("BUYER", 'Buyer'),
    )

    phone_regex = RegexValidator( regex = r'^(?:\+?88)?01[15-9]\d{8}$', message ="Phone number must be entered in the format +01777575801 up to 10 digits allowed.")
    phone       = models.CharField('Phone',validators =[phone_regex], max_length=10, unique = True,null=True)
    REQUIRED_FIELD = ['username','phone']


    objects = UserManager()
