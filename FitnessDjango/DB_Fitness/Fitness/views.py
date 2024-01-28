from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Datas

# Create your views here.
def home(request):
    return HttpResponse("Hello,Dinesh!")
  
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def proteintake(request):
    template = loader.get_template('proteintake.html')
    return HttpResponse(template.render())

def maintance(request):
    template = loader.get_template('maintance.html')
    return HttpResponse(template.render())

def bmi(request):
    template = loader.get_template('bmi.html')
    return HttpResponse(template.render())



 

def signup(request):  # 127.0.0.1:8000/
    mydata=Datas.objects.all()
    if(mydata!=""):
        return render(request,"signup.html",{"data":mydata})
    else:
        return render(request,"signup") 
      
    

def addData(request):
    mydata=Datas.objects.all()
    if request.method=="POST":
        name=request.POST["name"]
        dob=request.POST["dob"]
        phno=request.POST["phno"]
        email=request.POST["email"]
        password=request.POST["password"]
        conpass=request.POST["conpass"]
        
        obj=Datas()
        obj.Name=name
        obj.Dob=dob
        obj.Phno=phno
        obj.Email=email
        obj.Password=password
        obj.Conpass=conpass
        obj.save()
        return redirect("login")
    return render(request,"login.html",{"data":mydata})


def getdata(request):
    data = Datas.objects.values()
    return JsonResponse(list(data), safe=False)

