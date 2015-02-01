# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rota', models.IntegerField(max_length=5)),
            ],
            options={
                'verbose_name': 'coleta',
                'verbose_name_plural': 'coletas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ColetaHorario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coleta', models.ForeignKey(to='recmap.Coleta')),
            ],
            options={
                'verbose_name': 'coleta/Hor\xe1rio',
                'verbose_name_plural': 'coleta/hor\xe1rios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('csv_nome', models.CharField(max_length=100)),
                ('p_nome', models.CharField(max_length=200)),
                ('nome', models.CharField(unique=True, max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'endere\xe7o',
                'verbose_name_plural': 'endere\xe7os',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=15)),
                ('intervalo', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'verbose_name': 'hor\xe1rio',
                'verbose_name_plural': 'hor\xe1rios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_setor', models.CharField(max_length=10)),
                ('frequencia', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'setor',
                'verbose_name_plural': 'setores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coletahorario',
            name='horario',
            field=models.ForeignKey(to='recmap.Horario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coleta',
            name='endereco',
            field=models.ForeignKey(to='recmap.Endereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coleta',
            name='setor',
            field=models.ForeignKey(to='recmap.Setor'),
            preserve_default=True,
        ),
    ]
