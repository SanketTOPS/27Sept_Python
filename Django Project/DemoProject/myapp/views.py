from django.shortcuts import render, HttpResponse
import random

# Create your views here.

def index(request):
    #return HttpResponse("Welcome to TOPS!")
    #data={'nm':'Nirav'}
    data={'nm':random.randint(1111,9999)}
    return render(request,'index.html',data)
