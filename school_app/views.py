from django.shortcuts import render

# Create your views here.
def home(request):
    
    context = {

    }
    return render(request, 'school_app/home_page.html', context)