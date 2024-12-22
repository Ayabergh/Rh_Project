from django.contrib import admin

from .models import Personnel,Service,Congee,Evaluations,CritaireEvaluations

# Register your models here.

admin.site.register(Personnel) 
admin.site.register(Service) 
admin.site.register(Congee) 
admin.site.register(Evaluations) 
admin.site.register(CritaireEvaluations) 



