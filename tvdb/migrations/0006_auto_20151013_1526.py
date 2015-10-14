# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvdb', '0005_auto_20151013_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='poster',
            field=models.ImageField(upload_to='tvdb\\static\\posters'),
            preserve_default=True,
        ),
    ]
