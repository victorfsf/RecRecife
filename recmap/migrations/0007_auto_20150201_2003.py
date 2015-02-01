# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0006_auto_20150201_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='descricao',
            field=models.TextField(default=b'Sem descri\xc3\xa7\xc3\xa3o!', max_length=512),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default=b'None', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='enviado_por',
            field=models.CharField(default=b'An\xc3\xb4nimo', max_length=200),
            preserve_default=True,
        ),
    ]
