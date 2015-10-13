# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvdb', '0004_episode_episode_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='poster',
            field=models.ImageField(upload_to='tvdb'),
            preserve_default=True,
        ),
    ]
