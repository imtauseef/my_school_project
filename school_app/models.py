from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number = models.IntegerField(max_length=4)
    student_name = models.CharField(max_length=100, blank=False, null=False)
    grade_class = models.CharField(max_length=20, blank=False, null=False)
    email_id = models.CharField(max_length=100)
    student_phone = models.IntegerField(max_length=11)
    COURSES = (
        ("Arts", "Arts"),
        ("Computer Science", "Computer Science"),
        ("General Science", "General Science")
        )
    field_of_study = models.CharField(max_length=200, choices=COURSES)



class Teacher(models.Model):
    teacher_id = models.IntegerField(max_length=4, blank=False, null=False)
    teacher_name = models.CharField(max_length=100, blank=False, null=False)
    email_id = models.CharField(max_length=100, blank=False, null=False)
    teacher_phone = models.CharField(max_length=11, blank=False, null=False)
    subject_speciality = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200, blank=False, null=False)