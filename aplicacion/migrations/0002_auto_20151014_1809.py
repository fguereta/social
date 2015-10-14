# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacia',
            name='cuit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='farmacia',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
