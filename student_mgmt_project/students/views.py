from django.shortcuts import render
from django.http import HttpResponse
from .models import LoginForms
from django.contrib.auth import login,authenticate

def ViewAll(request):
    return render(request,"Home/Home.html")

def AddStudent(request):
    return render(request,"Home/Add_Student.html")

def UpdateStudent(request):
    return render(request,"Home/Update_Student.html")
def Register(request):
    return render(request,"register.html")
def RegisterStudent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username,password,name)
        return render(request,"login.html")

def LoginValue(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username,password)
    return render(request,"Home/Home.html")

def Login(request):
    return render(request,"login.html")