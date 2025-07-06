from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .models import Register,Students

GettingAllData = Students.objects.all()
AllStudents =[i.to_dict() for i in GettingAllData]

def ViewAll(request):
    all_students = Students.objects.all()
    all_students =[i.to_dict() for i in all_students]
    print({"Data":all_students})
    return render(request,"Home/Home.html",{"Data":AllStudents})

def Student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        RollNumber = request.POST.get('rollNumber')
        Department = request.POST.get('dept')
        dob = request.POST.get('dob')
        all_students = Students.objects.all()
        all_students =[i.to_dict() for i in all_students]
        isExisting = bool(list(filter(lambda x:x["Roll_Number"] == RollNumber,all_students)))
        if isExisting:
            return HttpResponse("❌ Roll Number Already Existed.")
        else:
            if True:
                register = Students(Name=name, Email=email, Roll_Number=RollNumber,Department=Department,Date_of_Birth=dob)
                register.save()
                return render(request,"Home/Home.html",{"Data":AllStudents})
def AddStudent(request):
    return render(request,"Home/Add_Student.html")

def UpdateStudent(request,studentId):
    print(studentId)
    return render(request,"Home/Update_Student.html")
def DeleteStudent(request,studentId):
    print(studentId)
    student = get_object_or_404(Students, Roll_Number=studentId)
    student.delete()
    return render(request,"Home/Home.html",{"Data":AllStudents})

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
            return render(request,"Home/Home.html",{"Data":AllStudents})
        else:
            return HttpResponse("❌ Invalid Id or Password")
def Login(request):
    return render(request,"login.html")