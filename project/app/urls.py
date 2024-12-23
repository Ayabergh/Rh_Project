from django.contrib import admin
from django.urls import  path
from . import views
from .views import main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('personnels/', views.personnels, name='personnels'),  # Personnels view
    path('personnels/add/', views.add_personnel, name='add_personnel'),  # Add personnel
    path('personnels/update/<int:id>/', views.update_personnel, name='update_personnel'),
    path('personnels/delete/<int:id>/', views.delete_personnel, name='delete_personnel'),
    path('personnels/<int:employee_id>/evaluations/', views.evaluations, name='evaluations'),
    path('personnels/<int:employee_id>/evaluations/add/', views.add_evaluation, name='add_evaluation'),
    path('evaluations/<int:evaluation_id>/report/', views.evaluation_report, name='evaluation_report'),

]