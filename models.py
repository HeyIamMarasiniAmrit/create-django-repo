from django.db import models

class profile(models.Model):
    name= models.CharField(max_length=30)
    email=models.EmailField(max_length=225)
    city=models.CharField(max_length=70)
    roll=models.IntegerField()
    state=models.CharField(max_length=70)
    comment = models.CharField(max_length=70, default='nothing')
