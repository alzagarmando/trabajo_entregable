# Generated by Django 4.0.5 on 2022-06-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemploLucaApp', '0002_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=30)),
            ],
        ),
    ]
