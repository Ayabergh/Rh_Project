# Generated by Django 5.1.4 on 2024-12-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_evaluation'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='period',
            field=models.CharField(choices=[('annual', 'Annual'), ('semi_annual', 'Semi-Annual')], default='annual', max_length=20),
        ),
    ]
