# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='display',
            field=models.BooleanField(default=False, verbose_name='DISPLAY COMPANY PUBLICLY ?'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='display',
            field=models.BooleanField(default=False, verbose_name='DISPLAY STAFF MEMBER PUBLICLY ?'),
        ),
    ]
