# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='endereco',
            field=models.ForeignKey(default=0, to='recmap.Endereco'),
            preserve_default=False,
        ),
    ]
