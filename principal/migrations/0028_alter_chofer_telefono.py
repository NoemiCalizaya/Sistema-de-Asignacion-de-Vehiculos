# Generated by Django 3.2 on 2023-05-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0027_alter_vehiculo_cilindrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='telefono',
            field=models.IntegerField(help_text='Introduzca el número de teléfono', unique=True),
        ),
    ]
