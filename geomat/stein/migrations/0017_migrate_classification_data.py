# -*- coding: utf-8 -*-
# Generated by Michael on 2016-11-05 14:00
from __future__ import unicode_literals

from django.db import migrations

"""
Move old data from 'classification1' field to new 'Classification' model
"""


def move_classification_data(apps, schema_editor):
    MineralType = apps.get_model("stein", "MineralType")
    Classification = apps.get_model("stein", "Classification")

    for mineral in MineralType.objects.all():
        classification = Classification(mineral_type=mineral, classification=mineral.classification1)
        classification.save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('stein', '0016_classification'),
    ]

    operations = [
        migrations.RunPython(move_classification_data)
    ]