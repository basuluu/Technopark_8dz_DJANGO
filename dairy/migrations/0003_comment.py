# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-13 16:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dairy', '0002_auto_20181213_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_сomment', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dairy.Post')),
            ],
        ),
    ]
