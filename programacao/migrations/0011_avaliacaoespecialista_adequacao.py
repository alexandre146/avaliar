# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacao', '0010_avaliacaoespecialista_gerada'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacaoespecialista',
            name='adequacao',
            field=models.CharField(default=None, max_length=50, null=True, blank=True, choices=[(b'0', b'Feedback gerado N\xc3\x83O \xc3\xa9 adequado'), (b'1', b'Feedback gerado \xc3\xa9 PARCIALMENTE adequado'), (b'2', b'Feedback gerado \xc3\xa9 TOTALMENTE adequado')]),
            preserve_default=True,
        ),
    ]
