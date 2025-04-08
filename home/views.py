from django.shortcuts import render
from django.http import HttpResponse
from .models import categories

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def plans(request):
    dict_cat = {
        'category' : categories.objects.all()
    }
    return render(request, 'plan.html', dict_cat)

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')