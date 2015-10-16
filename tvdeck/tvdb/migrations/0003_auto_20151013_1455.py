# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvdb', '0002_auto_20151013_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshow',
            name='avg_episode_rating',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='total_runtime',
        ),
    ]
