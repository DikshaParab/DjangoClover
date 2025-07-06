from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .models import Register
def ViewAll(request):
    return render(request,"Home/Home.html")

def AddStudent(request):
    return render(request,"Home/Add_Student.html")

def UpdateStudent(request):
    return render(request,"Home/Update_Student.html")
def Register(request):
    return render(request,"register.html")
from django.shortcuts import render
from django.http import HttpResponse
from .models import Register  # Ensure your model is imported

def RegisterStudent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('Repassword')
        all_students = Register.objects.all()
        all_students =[i.to_dict() for i in all_students]
        isExisting = bool(list(filter(lambda x:x["Email"] == username,all_students)))
        if isExisting:
            return HttpResponse("❌ Account Already Existed.")
        else:
            if password == repassword:
                register = Register(Name=name, Password=password, Email=username)
                register.save()
                return render(request, "login.html")  # Redirect or render as needed
            else:
                return HttpResponse("❌ Both passwords are different. Please try again.")
    
    return render(request, "register.html")  # If GET request, show registration form


def LoginValue(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        all_students = Register.objects.all()
        all_students =[i.to_dict() for i in all_students]
        isExisting = list(filter(lambda x:x["Email"] == username,all_students))
        if isExisting[0]["Password"] == password:
            return render(request,"Home/Home.html")
        else:
            return HttpResponse("❌ Invalid Id or Password")
        
def Login(request):
    return render(request,"login.html")