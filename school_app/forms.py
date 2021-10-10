from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput, NumberInput, Select
from .models import Student, Teacher

class UserForm(UserCreationForm):
    """creating a form for registeration."""

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class StudentForm(ModelForm):
    """making form from the model Student"""
    class Meta:
        model = Student
        fields = ["user", "student_name", "gradeclass", "email_id", "student_phone", "field_of_study"]
        widgets = {
            "user": Select(attrs={"class": "form-control", "placeholder": "user"}),
            "student_name": TextInput(attrs={"class": "form-control", "placeholder": "Student Name"}),
            "gradeclass": Select(attrs={"class": "form-control", "placeholder": "Grade Class"}),
            "email_id": EmailInput(attrs={"class": "form-control", "placeholder": "Email Id"}),
            "student_phone": TextInput(attrs={"class": "form-control", "placeholder": "Student Phone"}),
            "field_of_study": Select(attrs={"class": "form-control", "placeholder": "Field Of Study"}),
        }


class TeacherForm(ModelForm):
    """making form from the teacher models."""

    class Meta:
        model = Teacher
        fields = ["user", "teacher_name", "email_id", "teacher_phone", "subject_speciality", "qualification", "current_pat"]
        widgets = {
            "user": Select(attrs={"class": "form-control", "placeholder": "user", "required": "true"}),
            "teacher_name": TextInput(attrs={"class": "form-control", "placeholder": "Search Faculty"}),
            "email_id": EmailInput(attrs={"class": "form-control", "placeholder": "Email id", "required": "true"}),
            "teacher_phone": TextInput(attrs={"class": "form-control", "placeholder": "Phone number", "required": "true"}),
            "subject_speciality": TextInput(attrs={"class": "form-control", "placeholder": "Subject Speciality"}),
            "qualification": TextInput(attrs={"class": "form-control", "placeholder": "Qualification", "required": "true"}),
            "current_pat": Select(attrs={"class": "form-control", "placeholder": "Current PAT"}),
        }