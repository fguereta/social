# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Derivacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diagnostico', models.CharField(max_length=20)),
                ('prestacion', models.TextField(blank=True)),
                ('proposito', models.TextField(blank=True)),
                ('tipopaciente', models.CharField(max_length=12, choices=[(b'Internado', b'Internado'), (b'Ambulatorio', b'Ambulatorio')])),
                ('caracter', models.CharField(max_length=12, choices=[(b'Urgente', b'Urgente'), (b'A la brevedad', b'A la brevedad'), (b'Programado', b'Programado')])),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('hospital', models.CharField(max_length=20)),
                ('servicio', models.CharField(max_length=20)),
                ('contacto', models.CharField(max_length=20)),
                ('acompananate', models.CharField(max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('motivo', models.CharField(max_length=20)),
                ('tipotraslado', models.CharField(max_length=20, choices=[(b'Aereo', b'Aereo'), (b'Terrestre', b'Terrestre')])),
                ('transporteregular', models.CharField(max_length=20, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('trasladosanitario', models.CharField(max_length=20, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('condiciones', models.TextField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleSolicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('dosis', models.CharField(max_length=20)),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
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
                ('telefono', models.IntegerField(null=True, blank=True)),
                ('celular', models.IntegerField()),
                ('sexo', models.CharField(max_length=10, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
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
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalle', models.ForeignKey(to='aplicacion.DetalleSolicitud')),
            ],
        ),
        migrations.CreateModel(
            name='AccionSocial',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aplicacion.Persona')),
                ('legajo', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=20, choices=[(b'Supervisor', b'Supervisor'), (b'Operador', b'Operador')])),
            ],
            bases=('aplicacion.persona',),
        ),
        migrations.CreateModel(
            name='Farmaceutico',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='aplicacion.Persona')),
                ('farmacia', models.ForeignKey(to='aplicacion.Farmacia')),
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
            model_name='detallesolicitud',
            name='remedio',
            field=models.ForeignKey(to='aplicacion.Remedio'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='paciente',
            field=models.ForeignKey(to='aplicacion.Paciente'),
        ),
        migrations.AddField(
            model_name='detallesolicitud',
            name='medico',
            field=models.ForeignKey(to='aplicacion.Medico'),
        ),
        migrations.AddField(
            model_name='derivacion',
            name='paciente',
            field=models.ForeignKey(to='aplicacion.Paciente'),
        ),
    ]
