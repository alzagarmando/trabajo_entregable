# Generated by Django 4.0.5 on 2022-06-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemploLucaApp', '0003_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fechaDeEntrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
    ]
