# Generated by Django 3.2 on 2023-05-09 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0003_alter_asignacion_vehiculo_fecha'),
        ('principal', '0007_delete_categorialic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persona',
            new_name='Chofer',
        ),
    ]
