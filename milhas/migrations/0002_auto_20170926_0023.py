# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milhas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocao',
            name='data_promocao',
        ),
        migrations.AddField(
            model_name='promocao',
            name='data_promocao_fim',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='promocao',
            name='data_promocao_inicio',
            field=models.DateTimeField(null=True),
        ),
    ]
