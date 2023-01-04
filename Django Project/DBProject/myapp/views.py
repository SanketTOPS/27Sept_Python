from django.shortcuts import render,redirect
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

def updatedata(request,id):
    uid=usersignup.objects.get(id=id)
    if request.method=='POST':
        updateuser=signupForm(request.POST)
        if updateuser.is_valid():
            updateuser=signupForm(request.POST,instance=uid)
            updateuser.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'uid':usersignup.objects.get(id=id)})

def deletedata(request,id):
    uid=usersignup.objects.get(id=id)
    usersignup.delete(uid)
    return redirect('showdata')
