# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-06 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_user_details_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='contact_number',
        ),
    ]
