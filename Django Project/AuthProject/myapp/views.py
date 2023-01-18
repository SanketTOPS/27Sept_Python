from django.shortcuts import render,redirect
from .forms import usersignupForm
from .models import userSignup
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    user=request.session.get("user")
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        user=userSignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login successfull!")
            request.session["user"]=unm
            return redirect('home')
        else:
            print("Error!Plz try again")
    return render(request,'index.html',{'user':user})

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

#@login_required(login_url='/')
def home(request):
    user=request.session.get("user")
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def feedback(request):
    return render(request,'feedback.html')