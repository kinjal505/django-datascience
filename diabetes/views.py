import os
from statistics import linear_regression
from django.http import HttpResponse
from django.shortcuts import render
import joblib
import pickle


lr = joblib.load("static\\linear_regression")


# Create your views here.


def about(request):
    return render(request,"about.html")
    
def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")


def prediction(request):
    if request.method == "POST":
     age = int(request.POST.get('age'))   
     sex = int(request.POST.get('sex'))  
     bmi  = float(request.POST.get('BMI'))
     children = int(request.POST.get('children'))
     smoker = int(request.POST.get('smoker'))
     region = int(request.POST.get('Region'))
     print(age,sex,bmi,children,smoker,region) 
     pred=round(lr.predict([[age,sex,bmi,children,smoker,region]])[0])
     print(pred)
     output =  {"output" : pred }
     return render(request,"prediction.html",output)
    else:
         return render(request,"prediction.html")

def login(request):
    return render(request,"login.html")

def registration(request):
    return render(request,"registration.html")








