# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_auto_20151102_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallesolicitud',
            name='estado',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
