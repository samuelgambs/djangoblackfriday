# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milhas', '0013_auto_20171110_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cupom',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='cupom',
            name='code_cupom',
            field=models.CharField(max_length=20, unique=True, verbose_name='Código do Cupom'),
        ),
        migrations.AlterField(
            model_name='cupom',
            name='cupom_end_date',
            field=models.DateTimeField(null=True, verbose_name='Data Fim Cupom'),
        ),
        migrations.AlterField(
            model_name='cupom',
            name='cupom_start_date',
            field=models.DateTimeField(null=True, verbose_name='Data Início Cupom'),
        ),
        migrations.AlterField(
            model_name='cupom',
            name='sold_out',
            field=models.BooleanField(default=1, verbose_name='Esgotado'),
        ),
        migrations.AlterField(
            model_name='cupom',
            name='status',
            field=models.TextField(default='Últimas Passagens', max_length=20, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='cupom',
            name='subtitle',
            field=models.TextField(default='subtitulo', max_length=20, verbose_name='Para'),
        ),
        migrations.AlterField(
            model_name='cupom',
            name='title',
            field=models.TextField(default='título', max_length=20, verbose_name='Título'),
        ),
    ]
