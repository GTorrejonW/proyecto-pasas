from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate
 


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=150)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=255)
    #password1 = forms.TextInput(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Contraseña'})), 
    #password2 = forms.TextInput(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Reitere la contraseña'})),   

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2') 

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)    

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
   