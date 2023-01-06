from django.shortcuts import render,redirect
from .forms import usersignupForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=usersignupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User created successfully!")
            return redirect('home')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')