from django.contrib import admin
from .models import CustomUser, Student, Teacher, GradeNumber, ProjectsAndAssignments, CustomUser

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(GradeNumber)
admin.site.register(ProjectsAndAssignments)
admin.site.register(CustomUser)