# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0041_auto_20171102_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizanswer',
            name='feedback_correct',
            field=models.CharField(blank=True, default=b'', max_length=500, verbose_name='feedback if answered correctly'),
        ),
        migrations.AlterField(
            model_name='quizanswer',
            name='feedback_incorrect',
            field=models.CharField(blank=True, default=b'', max_length=500, verbose_name='feedback if answered incorrectly'),
        ),
    ]