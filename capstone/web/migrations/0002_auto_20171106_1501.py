# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Status',
        ),
        migrations.AddField(
            model_name='order_item',
            name='Status',
            field=models.CharField(default='CK', max_length=10),
        ),
    ]
