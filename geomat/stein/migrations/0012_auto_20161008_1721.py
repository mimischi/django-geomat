# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 15:21


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('stein', '0011_auto_20161008_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crystalsystem',
            name='pressure',
            field=models.IntegerField(blank=True, null=True, verbose_name='pressure'),
        ),
        migrations.AlterField(
            model_name='crystalsystem',
            name='temperature',
            field=models.IntegerField(blank=True, null=True, verbose_name='temperature'),
        ),
    ]
