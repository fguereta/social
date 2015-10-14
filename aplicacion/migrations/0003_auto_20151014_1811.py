# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_auto_20151014_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='derivacion',
            name='condiciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacimiento',
            field=models.DateField(),
        ),
    ]
