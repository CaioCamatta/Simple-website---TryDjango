# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=120),
        ),
    ]
