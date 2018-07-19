# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0013_auto_20180710_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigo',
            name='similaridade_jaccard',
            field=models.FloatField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codigo',
            name='similaridade_text',
            field=models.FloatField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codigo',
            name='similaridade_tree',
            field=models.FloatField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
