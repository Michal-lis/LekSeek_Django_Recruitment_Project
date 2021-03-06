# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20170620_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': 'movies'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': 'rooms'},
        ),
        migrations.AlterModelOptions(
            name='screening',
            options={'verbose_name_plural': 'screenings'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name_plural': 'tickets'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='screening',
            name='view_day',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=0),
        ),
    ]
