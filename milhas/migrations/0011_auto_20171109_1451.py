# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milhas', '0010_auto_20171108_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupom',
            name='sold_out',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='cupom',
            name='cupom_start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
