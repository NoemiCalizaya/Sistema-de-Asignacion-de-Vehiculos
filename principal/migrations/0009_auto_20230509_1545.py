# Generated by Django 3.2 on 2023-05-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_rename_persona_chofer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='ci',
            field=models.CharField(help_text='Introduzca el número de C.I.', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='chofer',
            name='direccion',
            field=models.CharField(blank=True, help_text='Introduzca la dirección', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chofer',
            name='telefono',
            field=models.CharField(help_text='Introduzca el número de teléfono', max_length=10),
        ),
    ]
