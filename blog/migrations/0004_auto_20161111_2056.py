# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='eggs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='flowers',
            field=models.IntegerField(default=0),
        ),
    ]