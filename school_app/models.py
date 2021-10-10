from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    """two fields modification in User model."""
    class Types(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        FACULTY = 'FACULTY', 'Faculty'
        ADMIN = 'ADMIN', 'Admin'

    types = models.CharField(max_length=50, choices=Types.choices, default=Types.ADMIN)
    user_id = models.CharField(max_length=20, blank=False, unique=True)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['types']

    def __str__(self):
        return self.user_id


class GradeNumber(models.Model):
    """ defining classroom number"""
    grade = models.CharField(max_length=2)


    def __str__(self):
        return self.grade + "th Grade"


class ProjectsAndAssignments(models.Model):
    """all list of assignments,projects or tests held in the school"""
    PAT = (
        ('Project', 'Project'),
        ('Assignment', 'Assignment'),
        ('Test', 'Test'),
    )
    pat_category = models.CharField(max_length=200, choices=PAT)
    pat_name = models.CharField(max_length=200, blank=True)
    for_grade = models.ForeignKey(GradeNumber, on_delete=models.CASCADE)


    def __str__(self):
        return self.pat_name

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=100, blank=False, null=False)
    email_id = models.CharField(max_length=100, blank=False, null=False)
    teacher_phone = models.IntegerField(null=True, blank=True, max_length=None)
    subject_speciality = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200, blank=False, null=False)
    current_pat = models.ForeignKey(ProjectsAndAssignments,blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, blank=False, null=False)
    gradeclass = models.ForeignKey(GradeNumber, on_delete=models.CASCADE)
    email_id = models.CharField(max_length=100)
    student_phone = models.IntegerField(null=True, blank=True,)
    COURSES = (
        ("Arts", "Arts"),
        ("Computer Science", "Computer Science"),
        ("General Science", "General Science"),
        )
    field_of_study = models.CharField(max_length=200, choices=COURSES)


    def __str__(self):
        return self.student_name
