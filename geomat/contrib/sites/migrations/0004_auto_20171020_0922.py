# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 09:22


import django.contrib.sites.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20170111_1319'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='site',
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
    ]