# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Derivacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diagnostico', models.CharField(max_length=20)),
                ('prestacion', models.TextField(blank=True)),
                ('proposito', models.TextField(blank=True)),
                ('tipopaciente', models.CharField(max_length=12, choices=[('Internado', 'Internado'), ('Ambulatorio', 'Ambulatorio')])),
                ('caracter', models.CharField(max_length=12, choices=[('Urgente', 'Urgente'), ('A la brevedad', 'A la brevedad'), ('Programado', 'Programado')])),
                ('fecha', models.CharField(max_length=20)),
                ('hora', models.CharField(max_length=10)),
                ('hospital', models.CharField(max_length=20)),
                ('servicio', models.CharField(max_length=20)),
                ('contacto', models.CharField(max_length=20)),
                ('acompanante', models.CharField(max_length=2, choices=[('Si', 'Si'), ('No', 'No')])),
                ('motivo', models.CharField(max_length=20)),
                ('tipotraslado', models.CharField(max_length=20, choices=[('Aereo', 'Aereo'), ('Terrestre', 'Terrestre')])),
                ('transporteregular', models.CharField(max_length=20, choices=[('Si', 'Si'), ('No', 'No')])),
                ('trasladosanitario', models.CharField(max_length=20, choices=[('Si', 'Si'), ('No', 'No')])),
                ('condiciones', models.TextField()),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=9)),
                ('cuil', models.CharField(max_length=15, null=True)),
                ('nacimiento', models.CharField(max_length=10, null=True)),
                ('nacionalidad', models.CharField(max_length=20, null=True)),
                ('correo', models.EmailField(max_length=254, null=True)),
                ('direccion', models.CharField(max_length=25, null=True)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('estado', models.CharField(max_length=20, null=True, blank=True)),
                ('sexo', models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])),
            ],
        ),
        migrations.CreateModel(
            name='Registro_estados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=10)),
                ('comentario', models.TextField(null=True, blank=True)),
                ('farmacia', models.ForeignKey(db_column='farmacia_id', blank=True, to='usuarios.UserFarmacia', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('generico', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
                ('presentacion', models.CharField(max_length=20)),
                ('observaciones', models.TextField(blank=True)),
                ('estado', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.CharField(max_length=30)),
                ('dosis', models.CharField(max_length=20)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('estado_aprobacion', models.CharField(max_length=15)),
                ('precio_solicitud', models.CharField(max_length=15)),
                ('farmacia', models.ForeignKey(db_column='farmacia_id', blank=True, to='usuarios.UserFarmacia', null=True)),
                ('remedio', models.ForeignKey(to='aplicacion.Remedio', db_column='remedio_id')),
            ],
        ),
        migrations.CreateModel(
            name='AccionSocial',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aplicacion.Persona')),
                ('legajo', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=20, choices=[('Supervisor', 'Supervisor'), ('Operador', 'Operador')])),
            ],
            bases=('aplicacion.persona',),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aplicacion.Persona')),
                ('especialidad', models.CharField(max_length=20)),
                ('matriculanacional', models.CharField(max_length=20)),
                ('matriculaprovincial', models.CharField(max_length=20)),
            ],
            bases=('aplicacion.persona',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aplicacion.Persona')),
                ('historiaclinica', models.CharField(max_length=20)),
                ('osocial', models.CharField(max_length=20)),
            ],
            bases=('aplicacion.persona',),
        ),
        migrations.AddField(
            model_name='registro_estados',
            name='solicitud',
            field=models.ForeignKey(to='aplicacion.Solicitud', db_column='solicitud_id'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='medico',
            field=models.ForeignKey(to='aplicacion.Medico', db_column='medico_id'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='paciente',
            field=models.ForeignKey(to='aplicacion.Paciente', db_column='paciente_id'),
        ),
        migrations.AddField(
            model_name='derivacion',
            name='paciente',
            field=models.ForeignKey(to='aplicacion.Paciente'),
        ),
    ]
