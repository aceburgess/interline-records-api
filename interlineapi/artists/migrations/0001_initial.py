# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.BooleanField(default=True, verbose_name='Public')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('cover_art', models.ImageField(blank=True, null=True, upload_to='cover-art-photos/')),
                ('release_date', models.DateField()),
                ('label', models.CharField(default='Interline Records', max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_artist', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='artist-photos/')),
                ('biography', models.TextField(blank=True, max_length=500, null=True)),
                ('contact_name', models.CharField(default='Interline Records', max_length=100, verbose_name='Contact / Management Name')),
                ('contact_link', models.URLField(default='https://www.interlinerecords.com', verbose_name='Contact / Management URL')),
                ('contact_email', models.EmailField(default='info@interlinerecords.com', max_length=254, verbose_name='Contact / Management Email')),
                ('website', models.URLField(blank=True, null=True)),
                ('spotify', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='YouTube')),
                ('bandcamp', models.URLField(blank=True, null=True)),
                ('itunes', models.URLField(blank=True, null=True, verbose_name='iTunes')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('soundcloud', models.URLField(blank=True, null=True)),
                ('vimeo', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.BooleanField(default=True, verbose_name='Public')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('video_service', models.CharField(choices=[('yt', 'Youtube'), ('vm', 'Vimeo')], default='yt', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='artists.Artist')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='artists.Artist'),
        ),
    ]
