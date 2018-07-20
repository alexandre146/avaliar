# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0009_remove_avaliacaoespecialista_gerada'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='gerada',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
