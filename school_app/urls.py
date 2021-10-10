from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home_page"),
    path('adminuser', views.adminuser, name="adminuser_page"),
    path('faculty', views.faculty, name="faculty_page"),
    path('student', views.student, name="student_page"),
    path('all_grades', views.all_grades, name="all_grades"),
    path('search_grade', views.search_grades_student, name="search_grade"),
    path('search_student', views.search_student, name="search_student"),
    path('search_faculty', views.search_faculty, name="search_faculty"),
    path('all_faculties', views.all_faculty, name="all_faculties"),
    
    path('register', views.register_user, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),

    path('student_profile', views.student_profile_view, name="studentprofileurl"),
    path('teacher_profile', views.teacher_profile_view, name="teacherprofileurl"),

    path('gallery', views.gallery, name="gallery"),
]
