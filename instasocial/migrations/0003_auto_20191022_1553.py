# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-22 15:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instasocial', '0002_auto_20191022_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userF',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
