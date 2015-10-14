# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvdb', '0003_auto_20151013_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='episode_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
