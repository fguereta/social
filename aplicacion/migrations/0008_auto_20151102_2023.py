# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_auto_20151026_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='estado',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacimiento',
            field=models.DateField(null=True),
        ),
    ]
