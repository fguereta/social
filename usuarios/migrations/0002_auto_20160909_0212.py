# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useroperador',
            old_name='operador',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='useroperador',
            name='categoria',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
