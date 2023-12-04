from django import forms
from .models import Post 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from moledordepasas import views


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('título', 'autor', 'cuerpo')
         
        widgets = {
            'título' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Aqui va el título'}),
            #'titletag' : forms.TextInput(attrs={'class':'form-control'}),
            #'autor' : forms.Select(attrs={'class':'form-control-plaintext'}),
            # Hide the author field in the form, we'll overwrite it later
            'autor': forms.HiddenInput(),
            'cuerpo' : forms.Textarea(attrs={'class':'form-control'}),
        }


        #def __init__(self, name, *args, **kwargs):
            #super().__init__(*args, **kwargs)
            #self.field['autor'].widget.attrs.update({'class': 'form-control', 'value': f'{name}'})

# html trash // <input type="text" id="autor" name="autor" maxlength="255" value="{{user.username}}" class="form-control" readonly>
            #<li><hr class="dropdown-divider"></li>
            #<li><a class="dropdown-item" href="{% url 'database' %}">View database</a></li>
            #<li><a class="dropdown-item" href="{% url 'inputAccount' %}">Register</a></li>
            
         