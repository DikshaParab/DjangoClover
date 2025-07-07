from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Register, Students

# Utility to return all students as dicts
def get_all_students():
    return [i.to_dict() for i in Students.objects.all()]

# Home view with all students
def view_all(request):
    return render(request, "Home/Home.html", {"Data": get_all_students()})

# Show login page
def login_form(request):
    return render(request, "login.html")

# Handle login submission
def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Register.objects.get(Email=email)
            if user.Password == password:
                return redirect("home")
            else:
                return HttpResponse("❌ Invalid Password")
        except Register.DoesNotExist:
            return HttpResponse("❌ Invalid Email")
    
    return redirect("login")

# Show registration page
def registration_form(request):
    return render(request, "register.html")

# Handle registration submission
def register_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('Repassword')

        if Register.objects.filter(Email=email).exists():
            return HttpResponse("❌ Account Already Exists.")

        if password != repassword:
            return HttpResponse("❌ Passwords do not match.")

        Register.objects.create(Name=name, Email=email, Password=password)
        return redirect("login")

    return render(request, "register.html")

# Show student creation form
def create_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_number = request.POST.get('rollNumber')
        department = request.POST.get('dept')
        dob = request.POST.get('dob')

        if Students.objects.filter(Roll_Number=roll_number).exists():
            return HttpResponse("❌ Roll Number Already Exists.")

        Students.objects.create(
            Name=name,
            Email=email,
            Roll_Number=roll_number,
            Department=department,
            Date_of_Birth=dob
        )
        return redirect("home")

    return render(request, "Home/Add_Student.html")

# Show student update form
def update_student_form(request, studentId):
    return render(request, "Home/Update_Student.html", {"ID": studentId})

# Handle student update
def update_student(request, studentId):
    if request.method == "POST":
        student = get_object_or_404(Students, Roll_Number=studentId)
        student.Name = request.POST.get("name")
        student.Email = request.POST.get("email")
        student.Roll_Number = request.POST.get("rollNumber")
        student.Department = request.POST.get("dept")
        student.Date_of_Birth = request.POST.get("dob")
        student.save()
        return redirect("home")

    return HttpResponse("❌ Invalid Request")

# Handle student deletion
def delete_student(request, studentId):
    student = get_object_or_404(Students, Roll_Number=studentId)
    student.delete()
    return redirect("home")
