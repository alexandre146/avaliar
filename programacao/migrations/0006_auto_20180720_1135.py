# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0005_auto_20180720_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_idx', models.IntegerField(default=None, null=True, blank=True)),
                ('especialista', models.ForeignKey(to='programacao.Especialista')),
                ('problema', models.ForeignKey(to='programacao.Problema')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrupoCodigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.ForeignKey(to='programacao.Codigo')),
                ('especialista', models.ForeignKey(to='programacao.Especialista')),
                ('grupo', models.ForeignKey(to='programacao.Grupo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='confirmar_feedback',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
