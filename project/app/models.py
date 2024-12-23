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


class Evaluation(models.Model):
    employee = models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name="evaluations")
    date = models.DateField(auto_now_add=True)
    evaluation_type = models.CharField(
        max_length=20,
        choices=[('Annual', 'Annual'), ('Semi-Annual', 'Semi-Annual')],
        default='Annual'
    )
    criteria = models.JSONField(default=dict)  # Customizable evaluation criteria in JSON format
    performance_rating = models.IntegerField()  # Performance rating, e.g., 1-10
    skills_developed = models.TextField(blank=True)  # Optional field for developed skills
    comments = models.TextField(blank=True)  # Manager's comments

    def __str__(self):
        return f"Evaluation for {self.employee.name} on {self.date}"



