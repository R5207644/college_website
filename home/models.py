from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    date=models.DateField()
    email=models.EmailField(default='test@gmail.com')
    sem=models.CharField(max_length=4,default='3rd')
    review=models.CharField(max_length=200,default='verry good website')