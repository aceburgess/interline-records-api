# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20170316_0642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='duty',
        ),
        migrations.AddField(
            model_name='company',
            name='business_type',
            field=models.CharField(blank=True, max_length=120, verbose_name='Type of Compnay'),
        ),
    ]
