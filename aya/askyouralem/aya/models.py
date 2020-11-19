from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    Topic = (
              ('Iman','Iman'),
              ('Quran','Quran'),
              ('Hadith','Hadith'),
              ('Taohid','Taohid'),
              ('Salat','Salat'),
    )

    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, null=True,on_delete= models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    body = models.TextField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    topic = models.CharField(max_length=200,choices=Topic)






    def __str__(self):
        return self.title