from django.db import models

# Create your models here.
#topic
#title
#body
#date
#user
class Question(models.Model):
    Topic = (
              ('Iman','Iman'),
              ('Quran','Quran'),
              ('Hadith','Hadith'),
              ('Taohid','Taohid'),
              ('Salat','Salat'),
    )



    title = models.CharField(max_length=200,null=True)
    body = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    user = models.CharField(max_length=200,null=True)
    topic = models.CharField(max_length=200,choices=Topic)
    def __str__(self):
        return self.title