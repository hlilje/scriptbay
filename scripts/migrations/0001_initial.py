# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=1024)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(max_length=8192)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('changed_date', models.DateTimeField(verbose_name='date changed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='script',
            field=models.ForeignKey(to='scripts.Script'),
            preserve_default=True,
        ),
    ]
