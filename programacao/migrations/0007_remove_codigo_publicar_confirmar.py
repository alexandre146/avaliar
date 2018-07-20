# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0006_auto_20180720_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigo',
            name='publicar_confirmar',
        ),
    ]
