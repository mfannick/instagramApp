# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-22 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instasocial', '0004_auto_20191022_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
