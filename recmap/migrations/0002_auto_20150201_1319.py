# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='csv_nome',
            new_name='nome_bruto',
        ),
        migrations.RenameField(
            model_name='endereco',
            old_name='p_nome',
            new_name='nome_min',
        ),
    ]
