# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tyrosine',
            name='percent_tyrosine',
            field=models.FloatField(),
        ),
    ]