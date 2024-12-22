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


class Congee(models.Model): 
    #leaveId = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    employe= models.ManyToManyField(Personnel, related_name="take") 
    leaveType= models.CharField(max_length=50) 
    startDate= models.DateField() 
    endDate= models.DateField() 
    status= models.CharField(max_length=50)

    def __str__(self):
        return f"Leave {self.leaveId}"
    

class Evaluations(models.Model):
    #evaluationId=  models.AutoField(primary_key=True)
    employe= models.ManyToManyField(Personnel, related_name="pass+") 
    period= models.CharField(max_length=50)
    goalsAchieved= models.CharField(max_length=254)
    comments= models.CharField(max_length=254)
    performanceScore= models.IntegerField()
    #report= models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.evaluationId
    


class CritaireEvaluations(models.Model):
    criteriaId= models.IntegerField()
    description= models.CharField(max_length=254)
    credit= models.IntegerField()
    def __str__(self):
        return self.criteriaId


 
