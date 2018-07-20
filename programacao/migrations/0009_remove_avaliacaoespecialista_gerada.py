# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0008_codigo_publicar_confirmar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacaoespecialista',
            name='gerada',
        ),
    ]
