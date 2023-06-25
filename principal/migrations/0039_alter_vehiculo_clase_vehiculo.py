# Generated by Django 3.2 on 2023-06-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0038_auto_20230530_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='clase_vehiculo',
            field=models.CharField(choices=[('1', 'MOTOCICLETA'), ('2', 'CAMIONETA'), ('3', 'VAGONETA'), ('4', 'CISTERNA'), ('5', 'CAMIÓN FRIGORÍFICO'), ('6', 'MAQUINARIA PESADA')], help_text='Seleccione la clase de vehículo', max_length=18),
        ),
    ]
