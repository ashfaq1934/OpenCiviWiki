# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-18 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20190418_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='bioguide_id',
            field=models.CharField(default='', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]