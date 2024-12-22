from django.shortcuts import render
from .models import Personnel
# Create your views here.
def main_page(request):
    return render(request, 'main/index.html')

def personnels(request):
    return render(request, 'employee/personnels.html')

def afficher_Personnel(request):             
    personnels = Personnel.objects.all() 
    return render(request,'employee/personnels.html',{"personnels":personnels}) 
