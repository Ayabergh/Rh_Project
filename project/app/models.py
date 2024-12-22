from django.db import models

# Create your models here.
class Service(models.Model):
    IdServic= models.CharField(max_length=50)
    nameservice= models.CharField(max_length=50) 

    def __str__(self):
        return self.IdServic

class Personnel(models.Model): 
    #employeId = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name= models.CharField(max_length=50) 
    Email= models.EmailField(max_length=254)
    Phone= models.IntegerField() 
    Position= models.CharField(max_length=40)
    skills= models.CharField(max_length=254) 
    training= models.CharField(max_length=254)
    IdService = models.ForeignKey(Service,on_delete=models.CASCADE)
    hireDate= models.DateField() 
    Adresse= models.CharField(max_length=254)
    
    def __str__(self):
        return self.name



    

