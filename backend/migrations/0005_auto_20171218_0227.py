# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_tag_date_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_taken',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]