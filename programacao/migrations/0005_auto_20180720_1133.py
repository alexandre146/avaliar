# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0004_remove_avaliacaoespecialista_confirmar_feedback'),
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
    ]
