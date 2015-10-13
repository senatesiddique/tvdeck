# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tvshow',
            old_name='runtime',
            new_name='total_runtime',
        ),
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tvshow',
            name='avg_episode_rating',
            field=models.DecimalField(max_digits=4, decimal_places=2, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episode',
            name='rating',
            field=models.DecimalField(max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='rating',
            field=models.DecimalField(max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
