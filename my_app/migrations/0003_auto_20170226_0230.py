# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-26 02:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20170226_0224'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('obj', 'email', 'comment')]),
        ),
    ]
