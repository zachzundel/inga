# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inga', '0008_auto_20160712_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='vouchers',
            field=models.ManyToManyField(blank=True, to='inga.Voucher'),
        ),
    ]