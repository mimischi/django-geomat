# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 09:54


import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0029_auto_20171010_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossaryentry',
            name='examples',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), help_text="When giving more than one example seperate them with a '|' ( Alt Gr + >-Button).", null=True, size=None, verbose_name='examples'),
        ),
    ]
