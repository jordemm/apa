# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 14:49
from __future__ import unicode_literals

import cartellaSociale.apps.cartellaSociale.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartellaSociale', '0006_auto_20170410_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donazioni',
            name='nasc',
            field=models.DateField(blank=True, null=True, validators=[cartellaSociale.apps.cartellaSociale.utils.validate_nascita], verbose_name='Data di Nascita'),
        ),
    ]
