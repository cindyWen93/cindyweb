# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='song',
            name='song_file',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='song',
            name='song_logo',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]