# Generated by Django 4.2.5 on 2023-11-26 23:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999)])),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, validators=[mainapp.models.validar_codigo])),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Numero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('estado', models.CharField(choices=[('PA', 'Pagado'), ('RE', 'Reservado'), ('DI', 'Disponible')], default='DI', max_length=2)),
                ('ganador', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=1500, null=True)),
                ('imagen', models.ImageField(upload_to='images/premio/')),
            ],
        ),
        migrations.CreateModel(
            name='Rifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=600)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('descripcion', models.CharField(max_length=1500)),
                ('imagen', models.ImageField(upload_to='images/rifa/')),
                ('estado', models.CharField(choices=[('OC', 'Oculta'), ('DI', 'Disponible'), ('FI', 'Finalizada'), ('AN', 'Anulada')], default='DI', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Premio_Rifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_premio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.premio')),
                ('id_rifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.rifa')),
            ],
        ),
        migrations.CreateModel(
            name='Numero_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.compra')),
                ('id_numero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.numero')),
            ],
        ),
        migrations.AddField(
            model_name='numero',
            name='id_rifa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.rifa'),
        ),
    ]