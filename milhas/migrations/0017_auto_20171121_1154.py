# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milhas', '0016_auto_20171121_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='message',
            field=models.TextField(default='Mensagem...', max_length=200, verbose_name='Mensagem'),
        ),
    ]
