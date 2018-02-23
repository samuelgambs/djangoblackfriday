# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milhas', '0003_auto_20170926_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promocao',
            options={'verbose_name': 'Promoção', 'verbose_name_plural': 'Promoções'},
        ),
        migrations.RemoveField(
            model_name='promocao',
            name='valor',
        ),
        migrations.RemoveField(
            model_name='promocao',
            name='valor_com_desconto',
        ),
        migrations.AddField(
            model_name='promocao',
            name='estado',
            field=models.TextField(default='Últimas Passagens'),
        ),
        migrations.AddField(
            model_name='promocao',
            name='subtitulo',
            field=models.TextField(default='subtitulo'),
        ),
    ]