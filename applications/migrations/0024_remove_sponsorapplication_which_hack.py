# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-25 18:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0023_fixes_to_applications_types_20200403_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorapplication',
            name='which_hack',
        ),
    ]
