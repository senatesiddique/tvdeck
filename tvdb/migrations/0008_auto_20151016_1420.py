# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvdb', '0007_auto_20151014_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
