# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_auto_20160830_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remedio',
            name='precio',
        ),
    ]
