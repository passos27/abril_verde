# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-23 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumdireito_app', '0004_auto_20180516_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palestrante',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='palestrante'),
        ),
    ]