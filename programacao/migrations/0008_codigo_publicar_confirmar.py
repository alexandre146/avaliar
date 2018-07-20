# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0007_remove_codigo_publicar_confirmar'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigo',
            name='publicar_confirmar',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
