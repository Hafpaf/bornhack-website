# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 08:55
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_auto_20170403_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epaycallback',
            name='payload',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
    ]
