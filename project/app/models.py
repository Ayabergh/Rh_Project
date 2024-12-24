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
    jours_restants = models.IntegerField(default=0) 
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.jours_restants < 0:
            self.jours_restants = 0  # Ensure no negative values
        super(Personnel, self).save(*args, **kwargs)


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


class Conge(models.Model):
    TYPES_CONGES = [
        ('Annuel', 'Congé Annuel'),
        ('Maladie', 'Congé Maladie'),
        ('Maternité', 'Congé Maternité'),
        ('Paternité', 'Congé Paternité'),
        ('Sans Solde', 'Congé Sans Solde'),
        ('Autre', 'Autre'),
    ]
    employe = models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name='conges')
    type_conge = models.CharField(max_length=20, choices=TYPES_CONGES)
    date_debut = models.DateField(verbose_name="Date de Début")
    date_fin = models.DateField(verbose_name="Date de Fin")
    jours_utilises = models.IntegerField(verbose_name="Jours Utilisés")
    jours_restants = models.IntegerField(verbose_name="Jours Restants", null=False)
    description = models.TextField(null=True, blank=True, verbose_name="Description")

    def save(self, *args, **kwargs):
        self.jours_utilises = (self.date_fin - self.date_debut).days + 1
        # Example calculation for jours_restants, adjust as per your business logic
        self.jours_restants = self.employe.jours_restants - self.jours_utilises
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employe.name} - {self.type_conge}"

