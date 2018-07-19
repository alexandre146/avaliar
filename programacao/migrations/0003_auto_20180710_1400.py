# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0002_auto_20180710_1357'),
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
        migrations.RemoveField(
            model_name='codigo',
            name='similaridade_jaccard',
        ),
        migrations.RemoveField(
            model_name='codigo',
            name='similaridade_text',
        ),
        migrations.RemoveField(
            model_name='codigo',
            name='similaridade_tree',
        ),
    ]
