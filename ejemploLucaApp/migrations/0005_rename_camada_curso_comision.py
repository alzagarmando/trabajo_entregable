# Generated by Django 4.0.5 on 2022-06-28 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemploLucaApp', '0004_entregable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='camada',
            new_name='comision',
        ),
    ]
