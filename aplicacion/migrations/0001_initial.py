# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razon_social', models.CharField(max_length=25)),
                ('cuit', models.IntegerField(blank=True)),
                ('direccion', models.CharField(max_length=25)),
                ('telefono', models.IntegerField(blank=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=9)),
                ('cuil', models.CharField(max_length=15)),
                ('nacimiento', models.DateField(blank=True)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True)),
                ('telefono', models.IntegerField(blank=True)),
                ('celular', models.IntegerField()),
                ('sexo', models.CharField(max_length=10, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
            ],
        ),
    ]