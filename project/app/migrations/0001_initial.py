# Generated by Django 5.1.4 on 2024-12-21 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CritaireEvaluations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteriaId', models.IntegerField()),
                ('description', models.CharField(max_length=254)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('Position', models.CharField(max_length=40)),
                ('skills', models.CharField(max_length=254)),
                ('training', models.CharField(max_length=254)),
                ('hireDate', models.DateField()),
                ('Adresse', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdServic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=50)),
                ('goalsAchieved', models.CharField(max_length=254)),
                ('comments', models.CharField(max_length=254)),
                ('performanceScore', models.IntegerField()),
                ('employe', models.ManyToManyField(related_name='pass+', to='app.personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Congee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveType', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('employe', models.ManyToManyField(related_name='take', to='app.personnel')),
            ],
        ),
        migrations.AddField(
            model_name='personnel',
            name='IdService',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service'),
        ),
    ]
