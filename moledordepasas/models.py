from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    age = models.IntegerField()


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