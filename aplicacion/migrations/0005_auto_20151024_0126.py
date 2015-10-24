# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0004_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField(null=True, blank=True)),
                ('categoria', models.CharField(max_length=20, choices=[(b'Supervisor', b'Supervisor'), (b'Operador', b'Operador'), (b'Farmaceutico', b'Farmaceutico')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
