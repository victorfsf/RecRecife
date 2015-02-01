# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0002_auto_20150201_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setor',
            old_name='nome_setor',
            new_name='nome',
        ),
    ]
