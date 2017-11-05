# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import geomat.stein.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stein', '0039_change_fractures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fracture',
            name='fracture',
            field=models.CharField(choices=[(b'CF', 'conchoidal'), (b'EF', 'earthy'), (b'HF', 'hackly'), (b'SF', 'splintery'), (b'UF', 'uneven')], max_length=2, null=True, verbose_name='fracture'),
        ),
        migrations.AlterField(
            model_name='mineraltype',
            name='cleavage',
            field=geomat.stein.fields.ChoiceArrayField(base_field=models.CharField(choices=[(b'PE', 'perfect'), (b'LP', 'less perfect'), (b'GO', 'good'), (b'DI', 'distinct'), (b'ID', 'indistinct'), (b'NO', 'none')], max_length=2), null=True, size=None, verbose_name='cleavage'),
        ),
        migrations.AlterField(
            model_name='mineraltype',
            name='lustre',
            field=geomat.stein.fields.ChoiceArrayField(base_field=models.CharField(choices=[(b'AM', 'adamantine lustre'), (b'DL', 'dull lustre'), (b'GR', 'greasy lustre'), (b'MT', 'metallic lustre'), (b'PY', 'pearly lustre'), (b'SL', 'silky lustre'), (b'SM', 'submetallic lustre'), (b'VT', 'vitreous lustre'), (b'WY', 'waxy lustre')], max_length=2), null=True, size=None, verbose_name='lustre'),
        ),
    ]