# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvdb', '0006_auto_20151013_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season_number', models.IntegerField(default=1)),
                ('tv_show', models.ForeignKey(to='tvdb.TVShow')),
            ],
        ),
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(to='tvdb.Season'),
        ),
    ]
