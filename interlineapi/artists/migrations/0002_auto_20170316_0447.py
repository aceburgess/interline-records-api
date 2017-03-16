# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='display_artist',
        ),
        migrations.AddField(
            model_name='artist',
            name='display',
            field=models.BooleanField(default=False, verbose_name='DISPLAY ARTIST PUBLICLY ?'),
        ),
        migrations.AlterField(
            model_name='album',
            name='display',
            field=models.BooleanField(default=True, verbose_name='PUBLIC ?'),
        ),
        migrations.AlterField(
            model_name='video',
            name='display',
            field=models.BooleanField(default=True, verbose_name='PUBLIC ?'),
        ),
    ]
