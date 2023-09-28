from django.shortcuts import render
from .models import Member

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
    plantilla = loader.get_template('register.html')
    return HttpResponse(plantilla.render({}, request))

def postAccount(request):
    name = request.POST['name']
    surname = request.POST['surname']
    email = request.POST['email']
    password = request.POST['password']
    account = Account(name=name,surname=surname,email=email,password=password)
    account.save()
    return HttpResponseRedirect(reverse('getAccount'))

def getAccount(request,id=0):
    if (id>0):
        accounts = list(Account.objects.filter(id=id).values())
        return render(request,"database.html",{"accounts":accounts})
    else:
        accounts = list(Account.objects.values())
        return render(request,"database.html",{"accounts":accounts})
    
def putAccount(request,id): 
    account = Account.objects.get(id=id)   
    plantilla = loader.get_template('change_register.html')
    context = {
        'account' : account
    }
    return HttpResponse(plantilla.render(context, request))

def putRegisterAccount(request,id):
    name = request.POST['name']
    surname = request.POST['surname']    
    email = request.POST['email']  
    account = Account.objects.get(id=id)
    account.name = name  
    account.surname = surname 
    account.email = email 
    account.save()
    return HttpResponseRedirect(reverse('getAccount'))  

def deleteAccount(request,id):
    account = Account.objects
    account.delete()
    return HttpResponseRedirect(reverse('getAccount')) 