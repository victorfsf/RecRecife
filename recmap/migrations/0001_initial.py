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
                ('ativo', models.BooleanField(default=True)),
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
                ('ativo', models.BooleanField(default=True)),
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
                ('nome_bruto', models.CharField(max_length=100)),
                ('nome_min', models.CharField(max_length=200)),
                ('nome', models.CharField(unique=True, max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'endere\xe7o',
                'verbose_name_plural': 'endere\xe7os',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enviado_por', models.CharField(default=b'An\xc3\xb4nimo', max_length=200)),
                ('email', models.EmailField(default=b'None', max_length=256)),
                ('situacao', models.CharField(max_length=256)),
                ('descricao', models.TextField(default=b'Sem descri\xc3\xa7\xc3\xa3o!', max_length=512)),
                ('ativo', models.BooleanField(default=True)),
                ('resolvido', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=15)),
                ('intervalo', models.CharField(unique=True, max_length=20)),
                ('ativo', models.BooleanField(default=True)),
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
                ('ativo', models.BooleanField(default=True)),
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
