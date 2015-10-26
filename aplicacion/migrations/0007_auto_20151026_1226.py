# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_auto_20151024_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cuil',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='observaciones',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
