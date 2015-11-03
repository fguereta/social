# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_auto_20151102_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='estado',
        ),
        migrations.AddField(
            model_name='farmacia',
            name='estado',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='estado',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
