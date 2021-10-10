from django import forms
from django.db.models.fields import CharField, TextField
from django.forms.widgets import TextInput
import django_filters
from .models import Student, Teacher
from .forms import StudentForm



class StudentFilter(django_filters.FilterSet):
    """making search filter to search all students of a grade class."""
    class Meta:
        model = Student
        fields = ['gradeclass',]
      
       
      


class TeacherFilter(django_filters.FilterSet):
    """making search filter to search teacher by name."""
    
    class Meta:
        models = Teacher
        fields = ['teacher_name',]
        