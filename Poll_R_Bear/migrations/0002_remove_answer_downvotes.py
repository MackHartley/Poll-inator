# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 05:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Poll_R_Bear', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='downvotes',
        ),
    ]