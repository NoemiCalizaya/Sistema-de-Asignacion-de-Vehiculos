# Generated by Django 3.2 on 2023-05-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0024_alter_vehiculo_cilindrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='cilindrada',
            field=models.PositiveIntegerField(help_text='Introduzca la cilindrada del vehiculo'),
        ),
    ]
