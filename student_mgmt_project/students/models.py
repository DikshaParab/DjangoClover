from django.db import models
from django import forms

# Create your models here.
class Students(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=200)
    Roll_Number = models.IntegerField()
    Department = models.CharField(max_length=120)
    Date_of_Birth = models.DateField()

class LoginForms(forms.Form):
    Email = forms.EmailField(max_length=120)
    Password = forms.CharField(max_length=120)
    