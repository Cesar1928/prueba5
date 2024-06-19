# Generated by Django 4.2.4 on 2024-05-26 13:20

import contact.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70, verbose_name='Nombre y Apellido')),
                ('lugar', models.CharField(max_length=100, verbose_name='Lugar')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('area', models.CharField(max_length=100, verbose_name='Área')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('subestandar', models.CharField(choices=[('CONDICIÓNSUBESTÁNDAR', 'Condición Sub-estándar'), ('ACTOSUBESTÁNDAR', 'Acto Sub-estándar')], max_length=80, verbose_name='Tipo De Evento')),
                ('empresa', models.CharField(choices=[('FAMESAEXPLOSIVOS', 'Famesa Explosivos'), ('TERCEROS', 'Terceros')], max_length=80, verbose_name='Empresa')),
                ('riesgo', models.CharField(choices=[('BAJO', 'Bajo'), ('MEDIO', 'Medio'), ('ALTO', 'Alto')], max_length=80, verbose_name='Riesgo')),
                ('descripcion', models.TextField(max_length=100, verbose_name='Descripción De Lo Sucedido')),
                ('accion', models.TextField(max_length=100, verbose_name='Plan De Acción')),
                ('recomendacion', models.TextField(max_length=80, verbose_name='Recomendación')),
                ('codigo', models.IntegerField(null=True, verbose_name='Código/DNI')),
                ('areareportante', models.CharField(blank=True, max_length=50, verbose_name='Área Reportante')),
                ('imagen', models.ImageField(upload_to=contact.models.mage)),
            ],
            options={
                'verbose_name_plural': 'Contact1s',
            },
        ),
    ]