# Generated by Django 3.2 on 2023-06-17 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0042_alter_vehiculo_clase_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='categoria_lic',
            field=models.CharField(choices=[('', '----Seleccione----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('M', 'M'), ('T', 'T'), ('A y M', 'A y M'), ('B y M', 'B y M'), ('C y M', 'C y M'), ('T y M', 'T y M'), ('AMT', 'AMT'), ('BMT', 'BMT'), ('CMT', 'CMT')], default='', help_text='Seleccione una categoría de licencia', max_length=5),
        ),
    ]
