# Generated by Django 3.2 on 2023-05-29 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0037_delete_cliente'),
        ('asignacion', '0015_auto_20230529_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambio_aceite',
            name='chofer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.chofer'),
        ),
        migrations.AddField(
            model_name='cambio_aceite',
            name='unidad_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.unidad'),
        ),
        migrations.AddField(
            model_name='cambio_aceite',
            name='vehiculo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.vehiculo'),
        ),
    ]
