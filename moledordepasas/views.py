from django.shortcuts import render
from .models import Account
from django.http import FileResponse
from http import HTTPStatus
from django.http import HttpResponseRedirect


from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

# Create your views here.
def index(request):
    return render(request, "moledordepasas/index.html")

def about(request):
    return render(request, "moledordepasas/about.html")

def database(request):
    return render(request, "moledordepasas/database.html")


# def login(request):
#     obj=Member.objects.all()
#     context={
#         "obj":obj,
#     }
#     return render(request, "moledordepasas/login.html",context)

def input(request):
    plantilla = get_template('moledordepasas/register.html')
    return HttpResponse(plantilla.render({}, request))

def postAccount(request):
    name = request.POST['name']
    surname = request.POST['surname']
    email = request.POST['email']
    age = request.POST['age']
    password = request.POST['password']
    account = Account(name=name,surname=surname,email=email,password=password,age=age)
    account.save()
    return HttpResponseRedirect(reverse('getAccount'))

def getAccount(request,id=0):
    if (id>0):
        accounts = list(Account.objects.filter(id=id).values())
        return render(request,"moledordepasas/database.html",{"accounts":accounts})
    else:
        accounts = list(Account.objects.values())
        return render(request,"moledordepasas/database.html",{"accounts":accounts})
    
def putAccount(request,id): 
    account = Account.objects.get(id=id)   
    plantilla = get_template('change_register.html')
    context = {
        'account' : account
    }
    return HttpResponse(plantilla.render(context, request))

def putRegisterAccount(request,id):
    name = request.POST['name']
    surname = request.POST['surname']    
    email = request.POST['email']  
    age = request.POST['age']
    account = Account.objects.get(id=id)
    account.name = name  
    account.surname = surname 
    account.email = email 
    account.age = age
    account.save()
    return HttpResponseRedirect(reverse('getAccount'))  

def deleteAccount(request,id):
    account = Account.objects.get(id=id)
    account.delete()
    return HttpResponseRedirect(reverse('getAccount')) 