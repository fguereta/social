# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_remove_remedio_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='medicamento_entregado',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='precio_solicitud',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
