# Generated by Django 3.2 on 2023-05-30 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0020_cambio_aceite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci_mecanico', models.CharField(max_length=10, unique=True)),
                ('nombres_mecanico', models.CharField(max_length=50)),
                ('ap_paterno_mecanico', models.CharField(max_length=30)),
                ('ap_materno_mecanico', models.CharField(blank=True, default=' ', max_length=30, null=True)),
                ('cargo', models.CharField(max_length=20)),
                ('telefono', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='asignacion_vehiculo',
            old_name='verificacion',
            new_name='verificacion_entrega',
        ),
        migrations.RemoveField(
            model_name='cambio_aceite',
            name='ap_materno_mecanico',
        ),
        migrations.RemoveField(
            model_name='cambio_aceite',
            name='ap_paterno_mecanico',
        ),
        migrations.RemoveField(
            model_name='cambio_aceite',
            name='autorizacion',
        ),
        migrations.RemoveField(
            model_name='cambio_aceite',
            name='lugar_revision',
        ),
        migrations.RemoveField(
            model_name='cambio_aceite',
            name='nombre_mecanico',
        ),
        migrations.AddField(
            model_name='asignacion_vehiculo',
            name='verificacion_devolucion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cambio_aceite',
            name='aprobado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cambio_aceite',
            name='caja',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cambio_aceite',
            name='corona',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cambio_aceite',
            name='maestranza',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='cambio_aceite',
            name='mecanico_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asignacion.mecanico'),
            preserve_default=False,
        ),
    ]
