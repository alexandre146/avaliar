# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0006_auto_20180710_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='codigo',
            name='medida_comments',
            field=models.FloatField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codigo',
            name='medida_multi',
            field=models.FloatField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
