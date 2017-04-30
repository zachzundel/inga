# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-20 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inga', '0008_auto_20170320_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uplcresult',
            name='all_inga',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='chemocoding',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='converted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Converted'),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='diva',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='extraction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Extraction'),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='mode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='ms_method',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='ms_mode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='project_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='raw',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.RAW'),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='sample_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='sample_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='tune_page',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uplcresult',
            name='uplc_method',
            field=models.TextField(blank=True, null=True),
        ),
    ]