# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor', models.FloatField()),
                ('valor_com_desconto', models.IntegerField()),
                ('codigo', models.CharField(max_length=10)),
                ('data_promocao', models.DateTimeField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('titulo', models.TextField()),
            ],
        ),
    ]
