# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='description',
            field=models.CharField(max_length=512, default='Hello Script'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='script',
            name='title',
            field=models.CharField(max_length=256, default='Hello Script'),
            preserve_default=False,
        ),
    ]
