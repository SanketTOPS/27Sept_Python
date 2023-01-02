from django.shortcuts import render
from .forms import signupForm
from .models import usersignup

# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid(): #true
            newuser.save()
            print("Your data has been saved!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    alldata=usersignup.objects.all()
    return render(request,'showdata.html',{'data':alldata})

def updatedata(request):
    return render(request,'updatedata.html')