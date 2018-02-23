# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milhas', '0015_msgadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='Mensagem...', max_length=20, verbose_name='Mensagem')),
            ],
        ),
        migrations.DeleteModel(
            name='MsgAdmin',
        ),
    ]
