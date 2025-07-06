from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('LoginInfo/', views.LoginValue, name='LoginValue'),
    path('Register/', views.Register, name='Register'),
    path('RegisterStudent/', views.RegisterStudent, name='RegisterStudent'),
    path('Home/', views.ViewAll, name='posts'),
    path('AddStudent/', views.AddStudent, name='AddStudents'),
    path('UpdateStudent/<int:studentId>/', views.UpdateStudent, name='UpdateStudent'),
    path('Student/', views.Student, name='Student'),
    path('DeleteStudent/<int:studentId>/', views.DeleteStudent, name='DeleteStudent'),
]
