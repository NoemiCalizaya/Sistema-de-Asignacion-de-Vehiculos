# Generated by Django 3.2 on 2023-05-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0026_alter_vehiculo_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='cilindrada',
            field=models.IntegerField(help_text='Introduzca la cilindrada del vehiculo'),
        ),
    ]
