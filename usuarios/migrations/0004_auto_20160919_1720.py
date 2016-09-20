# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_useroperador_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useroperador',
            old_name='nombre',
            new_name='direccion',
        ),
        migrations.AddField(
            model_name='useroperador',
            name='cuit',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useroperador',
            name='razon_social',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useroperador',
            name='telefono',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
