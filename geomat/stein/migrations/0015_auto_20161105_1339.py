# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 12:39


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('stein', '0014_auto_20161008_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mineraltype',
            old_name='classification',
            new_name='classification1',
        ),
    ]
