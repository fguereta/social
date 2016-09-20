# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20160909_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='useroperador',
            name='estado',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
