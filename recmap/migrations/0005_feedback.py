# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recmap', '0004_auto_20150201_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enviado_por', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=256)),
                ('situacao', models.CharField(max_length=256)),
                ('descricao', models.TextField(max_length=512)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
            bases=(models.Model,),
        ),
    ]
