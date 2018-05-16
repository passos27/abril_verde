# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-16 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumdireito_app', '0003_auto_20180516_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='palestrante',
            options={'verbose_name': 'Palestrante', 'verbose_name_plural': 'Palestrantes'},
        ),
        migrations.AlterModelOptions(
            name='palestras',
            options={'verbose_name': 'Palestra', 'verbose_name_plural': 'Palestras'},
        ),
        migrations.AddField(
            model_name='palestrante',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto_palestrante'),
        ),
        migrations.AlterField(
            model_name='palestras',
            name='descricao',
            field=models.TextField(blank=True, max_length=140, null=True, verbose_name='Descreva a palestra'),
        ),
    ]