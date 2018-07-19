# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0007_auto_20180710_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigo',
            name='medida_comments',
        ),
        migrations.RemoveField(
            model_name='codigo',
            name='medida_multi',
        ),
    ]
