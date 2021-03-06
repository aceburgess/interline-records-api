# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('link', models.URLField(blank=True)),
                ('public_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.BooleanField(default=False, verbose_name='Public')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('duty', models.CharField(blank=True, max_length=120, verbose_name='Service / Description')),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('website', models.URLField(blank=True)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff-photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Companies We Work With',
                'verbose_name_plural': 'Companies We Work With',
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.URLField()),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(blank=True, max_length=100)),
                ('site_description', models.CharField(blank=True, max_length=250)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('store', models.URLField(blank=True)),
                ('about_us', models.TextField(blank=True, max_length=600)),
                ('contact_name', models.CharField(blank=True, max_length=100)),
                ('contact_email', models.EmailField(blank=True, max_length=200)),
                ('background_photo_lp', models.ImageField(blank=True, upload_to='site-photos/', verbose_name='Background Photo Landing Page')),
                ('background_photo_mc', models.ImageField(blank=True, upload_to='site-photos/', verbose_name='Background Photo Artist Page')),
                ('background_photo_ad', models.ImageField(blank=True, upload_to='site-photos/', verbose_name='Background Photo Artist Detail Page')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.BooleanField(default=False, verbose_name='Public')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('job_title', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staff-photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
    ]
