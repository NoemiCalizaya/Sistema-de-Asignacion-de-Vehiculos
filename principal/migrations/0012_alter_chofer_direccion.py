# Generated by Django 3.2 on 2023-05-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_alter_chofer_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='direccion',
            field=models.CharField(blank=True, default=' ', help_text='Introduzca la dirección', max_length=50, null=True),
        ),
    ]
