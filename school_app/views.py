from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Student, Teacher, GradeNumber, ProjectsAndAssignments
from .filters import StudentFilter, TeacherFilter
from .forms import StudentForm, TeacherForm, UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CustomUser

# Create your views here.

def home(request):
    """this function consist of login form and other stuff home stuffs."""
    
    if request.method == "POST":
        user_id = request.POST.get('userid')
        user_type = request.POST.get('usertype')
        password = request.POST.get('userpassword')
        user = authenticate(request, user_id=user_id, types=user_type, password=password)
        if user is not None:
            login(request, user)
            if user_type == 'Student':
                return redirect('/student')
            elif user_type == 'Faculty':
                return redirect('/faculty')
            else:
                return redirect('/adminuser')
    
    context = {
    }
    return render(request, 'school_app/home_page.html', context)


def register_user(request):
    """this function consist of signup form."""
    user_id = request.POST.get("userid")
    user_type = request.POST.get("usertype")
    username = request.POST.get("username")
    password1 = request.POST.get("passwordone")
    password2 = request.POST.get("passwordtwo")
    if request.method == "POST":
        user = CustomUser.objects.create_user(user_id=user_id, username=username, types=user_type, password=password1)
        if user is not None:
            user.save()
            login(request, user)
            if user_type == "Student":
                return redirect('/student_profile')
            elif user_type == "Faculty":
                return redirect('/teacher_profile')
            else:
                return redirect('/')
    
    context = {}
    return render(request, 'school_app/register_page.html', context)


def login_user(request):
    user_id = request.POST.get('userid')
    user_type = request.POST.get('usertype')
    password = request.POST.get('userpassword')
    if request.method == "POST":
        user = authenticate(request, user_id=user_id, types=user_type, password=password)
        if user is not None:
            login(request, user)
            if user_type == 'Student':
                return redirect('/student')
            elif user_type == 'Faculty':
                return redirect('/faculty')
            else:
                return redirect('/adminuser')
            

    context = {}
    return render(request, 'school_app/login_page.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


def adminuser(request):
    context = {

    }
    return render(request, 'school_app/adminuser_page.html', context)


def faculty(request):
    fac_data = Teacher.objects.get(user_id=request.user)
    context = {
        "fac_data": fac_data,
    }
    return render(request, 'school_app/faculty_page.html', context)

@login_required(login_url='login')
def student_profile_view(request):
    """completing the profile of newly registered user."""
    grade_nums = GradeNumber.objects.all()
   
    if request.method == "POST":
        stForm = StudentForm(request.POST)
        if stForm.is_valid():
            stForm.save()
            return redirect("/student")
    else:
        stForm = StudentForm()
    context = {
        "grade_nums": grade_nums,
        "myform": stForm,
    }
    return render(request, 'school_app/student_profile_page.html', context)

@login_required(login_url='login')
def teacher_profile_view(request):
    """profile form for newly registered user."""

    if request.method == "POST":
        tForm = TeacherForm(request.POST)
        if tForm.is_valid():
            tForm.save()
            return redirect("/faculty")
    else:
        tForm = TeacherForm()
    context = {
        "myform": tForm,
    }
    return render(request, 'school_app/faculty_profile_page.html', context)

@login_required(login_url='login')
def student(request):
    """fetching data from student model"""
    st_data = Student.objects.get(user_id=request.user)


    context = {
        "st_data": st_data,
    }
    return render(request, 'school_app/student_page.html', context)

@login_required(login_url='login')
def search_grades_student(request):
    """fetching grade number and then explore all of its students."""
    grade_nums = GradeNumber.objects.all()
    all_students = Student.objects.all()
    select_data = request.POST.get('s_grade')
    all_students_searched = all_students.filter(gradeclass=select_data)
    """gradeFilter = StudentFilter(request.POST, queryset=all_students)
    all_students_searched = gradeFilter.qs"""

    context = {
        "all_students_searched": all_students_searched,
        #"gradeFilter": gradeFilter,
        'grade_nums': grade_nums,
    }
    return render(request, 'school_app/search_grade_page.html', context)


def gallery(request):
    context = {}
    return render(request, 'school_app/gallery_page.html', context)


@login_required(login_url='login')
def search_faculty(request):
    """searching for the concern teacher. """
    all_teachers = Teacher.objects.all()
    a_teacher = all_teachers.filter(teacher_name=request.POST.get('facultyname', False))

    """teacherFilter = TeacherFilter(request.GET, queryset=all_teachers)
    all_teachers_searched = teacherFilter.qs"""
    context = {
        #"teacherFilter": teacherFilter,
        "all_teachers_searched": a_teacher,
    }
    return render(request, 'school_app/search_faculty_page.html', context)


@login_required(login_url='login')
def search_student(request):
    """searching for the concern student."""
    all_students = Student.objects.all()
    a_student = all_students.filter(student_name=request.POST.get('studentname'))

    context = {
        'student_searched': a_student,
    }
    return render(request, 'school_app/search_student_page.html', context)

@login_required(login_url='login')
def all_faculty(request):
    all_teachers = Teacher.objects.all()

    context = {
        "all_teachers": all_teachers,
    }
    return render(request, 'school_app/all_faculties_page.html', context)

@login_required(login_url='login')
def all_grades(request):
    """detail of all grades in school. """
    all_students = Student.objects.all()
    
    context = {
        "all_students": all_students,
    }
    return render(request, 'school_app/all_grades_page.html', context)