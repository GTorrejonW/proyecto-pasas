from typing import Any
from django.shortcuts import render
from .models import Account
from django.http import FileResponse
from http import HTTPStatus
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from moledordepasas.forms import PostForm


# Create your views here.
def index(request):
    return render(request, "moledordepasas/index.html")

def about(request):
    return render(request, "moledordepasas/about.html")

def database(request):
    return render(request, "moledordepasas/database.html")

class tutpage(ListView):
    model = Post
    template_name = 'moledordepasas/tuts.html'
    ordering = ['likes']

class tutdetailview(DetailView):
    model = Post
    template_name = 'moledordepasas/tutsdet.html'

    def get_context_data(self, *args, **kwargs):
        context = super(tutdetailview, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])  
        total_likes = stuff.total_likes()     
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context 

class addtutview(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'moledordepasas/tutsadd.html' 
    #fields = '__all__' 
    #fields =  ('title', 'body', 'autor')  
    #find a way to avoid nullconstant with author on automatic detection 

class updatetutview(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'moledordepasas/tutsedit.html' 
    #fields = '__all__' 
    #fields =  ('title', 'body', 'autor')  
    #find a way to avoid nullconstant with author on automatic detection 

class tutdelete(DeleteView):
    model = Post
    template_name = 'moledordepasas/tutdelete.html'    
    success_url = reverse_lazy('tutorials')   

def tutlike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:    
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('tutsdet', args=[str(pk)]))


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

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        results = Post.objects.filter(título__icontains=searched)
        return render(request, 'moledordepasas/tutsearch.html',{'searched':searched, 'results':results}) 
    else:
        return render(request, 'moledordepasas/tutsearch.html',{}) 