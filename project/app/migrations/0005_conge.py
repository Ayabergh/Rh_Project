# Generated by Django 5.1.4 on 2024-12-24 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_evaluationcriteria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_conge', models.CharField(choices=[('Annuel', 'Congé Annuel'), ('Maladie', 'Congé Maladie'), ('Maternité', 'Congé Maternité'), ('Paternité', 'Congé Paternité'), ('Sans Solde', 'Congé Sans Solde'), ('Autre', 'Autre')], max_length=20)),
                ('date_debut', models.DateField(verbose_name='Date de Début')),
                ('date_fin', models.DateField(verbose_name='Date de Fin')),
                ('jours_utilises', models.IntegerField(verbose_name='Jours Utilisés')),
                ('jours_restants', models.IntegerField(verbose_name='Jours Restants')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conges', to='app.personnel')),
            ],
        ),
    ]
