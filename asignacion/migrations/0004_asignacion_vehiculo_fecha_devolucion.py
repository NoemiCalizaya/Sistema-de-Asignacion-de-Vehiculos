# Generated by Django 3.2 on 2023-05-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0003_alter_asignacion_vehiculo_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion_vehiculo',
            name='fecha_devolucion',
            field=models.DateField(blank=True, null=True),
        ),
    ]
