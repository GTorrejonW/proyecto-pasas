from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.http import FileResponse
from http import HTTPStatus
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
            # Redirect to a success page.
        else:
            messages.success(request, ("Hubo un error al logear, intentalo denuevo"))
            return redirect('login')
            # Return an 'invalid login' error message.
    else:
         return render(request, 'auth/login.html', {})
def logout_user(request):
    logout(request)
    messages.success(request, ("Sesión cerrada"))    
    return redirect('index')

def register_user(request):
  
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registrado!"))
            return redirect('index')
    else:
        form = UserCreationForm()    
    return render(request, 'auth/register_user.html', { 
        'form':form,
        })
