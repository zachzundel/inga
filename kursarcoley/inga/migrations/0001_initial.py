# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 23:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('chemistry_number', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('exp_min', models.TextField(blank=True, null=True)),
                ('exp_max', models.TextField(blank=True, null=True)),
                ('fwg', models.TextField(blank=True, null=True)),
                ('exp_vs_mat', models.TextField(blank=True, null=True)),
                ('use_field', models.TextField(blank=True, null=True)),
                ('cur_w', models.FloatField(blank=True, null=True)),
                ('vial_w', models.FloatField(blank=True, null=True)),
                ('box_number', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('extracted', models.NullBooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Chlorophyll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('percent_expansion', models.IntegerField(blank=True, null=True)),
                ('spadd', models.IntegerField(blank=True, null=True)),
                ('chl_mg_dm2', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Converted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('converted_file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('sequence', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('extraction_number', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('method', models.FloatField(blank=True, null=True)),
                ('chemist', models.CharField(blank=True, max_length=20, null=True)),
                ('notebook_number', models.IntegerField(blank=True, null=True)),
                ('extraction_notebook_number', models.IntegerField(blank=True, null=True)),
                ('page_number', models.IntegerField(blank=True, null=True)),
                ('dry_weight', models.FloatField(blank=True, default=0, null=True)),
                ('empty_vial_weight', models.FloatField(blank=True, default=0, null=True)),
                ('final_weight', models.FloatField(blank=True, default=0, null=True)),
                ('dry_marc_weight', models.FloatField(blank=True, default=0, null=True)),
                ('mass_extracted', models.FloatField(blank=True, default=0, null=True)),
                ('proportion_remaining', models.FloatField(blank=True, default=0, null=True)),
                ('percent_extracted', models.FloatField(blank=True, default=0, null=True)),
                ('box', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('chemistry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Chemistry')),
                ('other_chemistry', models.ManyToManyField(blank=True, db_constraint=False, related_name='other_chemistry', to='inga.Chemistry')),
                ('parent_extraction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Extraction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtractionResultWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('trait', models.CharField(max_length=100)),
                ('measurement', models.FloatField(blank=True, default=0, null=True)),
                ('extraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Extraction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtrafloralNectaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('basal_mm', models.FloatField(blank=True, null=True)),
                ('mid_mm', models.FloatField(blank=True, null=True)),
                ('apical_mm', models.FloatField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=25, null=True)),
                ('shape', models.TextField(blank=True, null=True)),
                ('efn_type', models.TextField(blank=True, null=True)),
                ('xEFN_mm', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeatureTableRawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('species_code_sample', models.CharField(max_length=30)),
                ('RT', models.FloatField()),
                ('MZ', models.FloatField()),
                ('PC_ID', models.CharField(max_length=30)),
                ('TIC', models.FloatField()),
                ('Date_Update', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('original_id', models.CharField(max_length=20)),
                ('exp_vs_mat', models.TextField()),
                ('exp_min', models.TextField()),
                ('exp_max', models.TextField()),
                ('efn', models.IntegerField()),
                ('ants', models.IntegerField()),
                ('ants_efn', models.FloatField()),
                ('ant_collection_number', models.TextField()),
                ('herbivores_present', models.BooleanField()),
                ('notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HerbivoreCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('photo', models.FileField(upload_to='')),
                ('analysis', models.CharField(max_length=100)),
                ('motu', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HerbivoreCollectionObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('herbivores_collected', models.IntegerField()),
                ('herbivores_total', models.IntegerField()),
                ('preliminary_family', models.CharField(max_length=20)),
                ('collection_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.HerbivoreCollection')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Field')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HerbivoreDNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('marker_gene', models.TextField()),
                ('fasta', models.FileField(upload_to='')),
                ('genbank', models.URLField()),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.HerbivoreCollection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HerbivoreSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('la_motu', models.TextField()),
                ('consensus_sequence', models.TextField()),
                ('blasting_family', models.TextField()),
                ('blasting_subfamily', models.TextField()),
                ('blasting_genus', models.TextField()),
                ('percentage_match_on_BOLD', models.IntegerField()),
                ('bin', models.TextField()),
                ('notes_on_host', models.TextField()),
                ('notes', models.TextField()),
                ('ibol', models.TextField()),
                ('motu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.HerbivoreCollection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Herbivory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('leaves_leaflets', models.IntegerField()),
                ('total', models.IntegerField()),
                ('x_herbivory', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HPLCResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('sample_type', models.CharField(max_length=100)),
                ('file_path', models.FileField(upload_to='')),
                ('date', models.DateField()),
                ('method', models.CharField(max_length=100)),
                ('column_used', models.CharField(max_length=100)),
                ('tyrosine', models.IntegerField()),
                ('extraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Extraction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeafMassArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('inches', models.FloatField(blank=True, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('dw_g', models.FloatField(blank=True, null=True)),
                ('dw_area_g', models.FloatField(blank=True, null=True)),
                ('drying_method', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('gps', models.IntegerField()),
                ('trail', models.IntegerField()),
                ('measure', models.IntegerField()),
                ('offset', models.IntegerField()),
                ('side', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('method_number', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nitrogen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('exp_vs_mat', models.TextField(blank=True, null=True)),
                ('weight_before_grounding', models.FloatField(blank=True, null=True)),
                ('percentage_of_expansion', models.TextField(blank=True, null=True)),
                ('weight_after_grounding', models.FloatField(blank=True, null=True)),
                ('sample_number_for_nitrogen_analysis', models.TextField(blank=True, null=True)),
                ('subsample_weight', models.FloatField(blank=True, null=True)),
                ('percent_nitrogen', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('chemistry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Chemistry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PC_ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('MZ_RT', models.TextField(blank=True, null=True)),
                ('Percent_TIC', models.FloatField(blank=True, null=True)),
                ('ms_ms_spec', models.TextField(blank=True, null=True)),
                ('ms_ms_spec_id', models.IntegerField(blank=True, null=True)),
                ('PC_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.FeatureTableRawData')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('plant_number', models.IntegerField(blank=True, null=True)),
                ('collectors', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('size', models.TextField(blank=True, null=True)),
                ('height', models.TextField(blank=True, null=True)),
                ('light', models.TextField(blank=True, null=True)),
                ('dbh', models.TextField(blank=True, null=True)),
                ('living_herbarium', models.TextField(blank=True, null=True)),
                ('dna', models.TextField(blank=True, null=True)),
                ('date_dna_sent', models.DateField(blank=True, null=True)),
                ('herbarium_sample', models.TextField(blank=True, null=True)),
                ('flower_color', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('new_leaves', models.IntegerField(blank=True, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlantDNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('dna', models.TextField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlantPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('photo', models.FileField(upload_to='')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlantSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('old_species_number', models.TextField(blank=True, null=True)),
                ('species_code', models.TextField(blank=True, null=True)),
                ('genus', models.TextField(blank=True, null=True)),
                ('species_name', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('authority', models.TextField(blank=True, null=True)),
                ('note_chemistry_analysis', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlantVoucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('voucher', models.CharField(max_length=10)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RAW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('raw_file_path', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('site', models.CharField(blank=True, max_length=12, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('latitude_degrees', models.TextField(blank=True, null=True)),
                ('latitude_minutes', models.IntegerField(blank=True, null=True)),
                ('longitude_degrees', models.TextField(blank=True, null=True)),
                ('longitude_minutes', models.IntegerField(blank=True, null=True)),
                ('altitude', models.IntegerField(blank=True, null=True)),
                ('temp', models.FloatField(blank=True, null=True)),
                ('annual_rainfall', models.IntegerField(blank=True, null=True)),
                ('rainfall_seasonality', models.TextField(blank=True, null=True)),
                ('rainfall_seasonality_pdfs', models.TextField(blank=True, null=True)),
                ('soils', models.TextField(blank=True, null=True)),
                ('solid_pdfs', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Toughness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('toughness', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tyrosine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('percent_tyrosine', models.FloatField()),
                ('file', models.TextField()),
                ('calibration', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('extraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Extraction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UPLCResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateField(auto_now=True)),
                ('generic', models.BooleanField(default=False)),
                ('diva', models.TextField()),
                ('date', models.DateField()),
                ('mode', models.TextField()),
                ('sample_type', models.TextField()),
                ('sample_id', models.TextField()),
                ('tune_page', models.TextField()),
                ('project_name', models.TextField()),
                ('ms_method', models.TextField()),
                ('uplc_method', models.TextField()),
                ('ms_mode', models.IntegerField()),
                ('notes', models.TextField()),
                ('all_inga', models.TextField()),
                ('chemocoding', models.TextField()),
                ('converted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Converted')),
                ('extraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Extraction')),
                ('raw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.RAW')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='plant',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Site'),
        ),
        migrations.AddField(
            model_name='plant',
            name='species_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.PlantSpecies'),
        ),
        migrations.AddField(
            model_name='location',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_plant', to='inga.Plant'),
        ),
        migrations.AddField(
            model_name='leafmassarea',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant'),
        ),
        migrations.AddField(
            model_name='herbivory',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Location'),
        ),
        migrations.AddField(
            model_name='herbivory',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.PlantSpecies'),
        ),
        migrations.AddField(
            model_name='herbivorecollection',
            name='collection_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.HerbivoreCollectionObservation'),
        ),
        migrations.AddField(
            model_name='hairs',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant'),
        ),
        migrations.AddField(
            model_name='field',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant'),
        ),
        migrations.AddField(
            model_name='featuretablerawdata',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.UPLCResult'),
        ),
        migrations.AddField(
            model_name='extrafloralnectaries',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inga.Plant'),
        ),
        migrations.AddField(
            model_name='chlorophyll',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Plant'),
        ),
        migrations.AddField(
            model_name='chemistry',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Plant'),
        ),
    ]
