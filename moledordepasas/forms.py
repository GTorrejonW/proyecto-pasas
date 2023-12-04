from django import forms
from .models import Post 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('título', 'autor', 'cuerpo')
        widgets = {
            'título' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Aqui va el título'}),
            #'titletag' : forms.TextInput(attrs={'class':'form-control'}),
            'autor' : forms.Select(attrs={'class':'form-control'}),
            'cuerpo' : forms.Textarea(attrs={'class':'form-control'}),
        }


    