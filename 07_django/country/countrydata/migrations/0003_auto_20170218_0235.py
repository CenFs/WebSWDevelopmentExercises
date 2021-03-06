# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrydata', '0002_auto_20170218_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='continent',
            old_name='countries',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='countrydata.Continent'),
        ),
    ]
