from django.contrib import admin
from django.urls import  path
from . import views
from .views import main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('personnels/', views.personnels, name='personnels'),  # Personnels view
    path('list_personnel',views.afficher_Personnel, name='list_personnel'), 

]