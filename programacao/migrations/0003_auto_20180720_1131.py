# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import programacao.validators


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0002_auto_20180720_1129'),
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
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='confirmar_nota',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='gerada',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='nova_nota',
            field=models.FloatField(default=None, null=True, blank=True, validators=[programacao.validators.valida_avaliacao]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='novo_feedback',
            field=models.TextField(default=None, max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codigo',
            name='publicar_confirmar',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
