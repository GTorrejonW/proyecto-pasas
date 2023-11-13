from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor.fields import CKEditorWidget

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    age = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    #titletag = models.CharField(max_length=200, default="Tutoriales")
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = RichTextField(blank=True, null=True)
    #image = models.ImageField(null =True, blank=True)
    
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('tutsdet', args=(str(self.id)))
        return reverse('tutorials')


# class Entity1(models.Model):
#    attribute1 = models.AutoField(primary_key=True)

#    def _str_(self):
#        return self.attribute1
    
#class Entity2(models.Model):  
#    attribute1 = models.AutoField(primary_key=True)
#    attribute2 = models.CharField(max_length=10)
#    attribute3 = models.ForeignKey(Entity1, on_delete=models.CASCADE, db_column='attribute1')  
#        
#    def _str_(self):
#         return self.attribute1, self.attribute2, self.attribute3

#THESE DONT WORK BTW