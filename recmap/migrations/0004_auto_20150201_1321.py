# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0003_auto_20150201_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setor',
            old_name='nome',
            new_name='nome_setor',
        ),
    ]
