# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-28 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inga', '0011_auto_20170320_1922'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plant',
            unique_together=set([('site', 'plant_number')]),
        ),
    ]
