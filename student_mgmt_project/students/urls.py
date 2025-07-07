from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form, name='login'),
    path('login/', views.login_user, name='login_user'),

    path('register/', views.registration_form, name='registration_form'),
    path('register/submit/', views.register_student, name='register_student'),

    path('home/', views.view_all, name='home'),
    
    path('students/add/', views.create_student, name='create_student'),
    path('students/update/<int:studentId>/', views.update_student_form, name='update_student_form'),
    path('students/update/submit/<int:studentId>/', views.update_student, name='update_student'),
    path('students/delete/<int:studentId>/', views.delete_student, name='delete_student'),
]
