# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0003_auto_20180720_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacaoespecialista',
            name='confirmar_feedback',
        ),
    ]
