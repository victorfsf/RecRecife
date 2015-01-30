# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0002_auto_20150130_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='csv_nome',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='p_nome',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
