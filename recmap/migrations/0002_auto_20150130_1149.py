# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='latitude',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='longitude',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
