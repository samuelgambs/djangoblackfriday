# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milhas', '0011_auto_20171109_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupom',
            name='max_oferta',
            field=models.BooleanField(default=0),
        ),
    ]