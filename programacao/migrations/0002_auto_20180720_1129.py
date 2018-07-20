# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='especialista',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='problema',
        ),
        migrations.RemoveField(
            model_name='grupocodigo',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='grupocodigo',
            name='especialista',
        ),
        migrations.RemoveField(
            model_name='grupocodigo',
            name='grupo',
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
        migrations.DeleteModel(
            name='GrupoCodigo',
        ),
        migrations.RemoveField(
            model_name='avaliacaoespecialista',
            name='confirmar_feedback',
        ),
        migrations.RemoveField(
            model_name='avaliacaoespecialista',
            name='confirmar_nota',
        ),
        migrations.RemoveField(
            model_name='avaliacaoespecialista',
            name='gerada',
        ),
        migrations.RemoveField(
            model_name='avaliacaoespecialista',
            name='nova_nota',
        ),
        migrations.RemoveField(
            model_name='avaliacaoespecialista',
            name='novo_feedback',
        ),
        migrations.RemoveField(
            model_name='codigo',
            name='publicar_confirmar',
        ),
    ]
