# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-13 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vision',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='KOTANIII', max_length=200),
        ),
    ]
