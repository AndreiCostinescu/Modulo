# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0003_auto_20170314_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='exam',
            field=models.IntegerField(choices=[(0, 'Written exam'), (1, 'Oral exam'), (2, 'paper'), (3, 'Other'), (4, '')], default=0),
        ),
        migrations.AlterField(
            model_name='module',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('DE', 'German'), ('', '')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='module',
            name='place',
            field=models.IntegerField(choices=[(0, 'Freising'), (1, 'Garching'), (2, 'Garching-Hochbrück'), (3, 'Inner city'), (4, 'Other'), (5, '')], default=None),
        ),
        migrations.AlterField(
            model_name='module',
            name='type',
            field=models.IntegerField(choices=[(0, 'Seminar'), (1, 'Workshop'), (2, 'Colloquium'), (3, 'Module'), (4, 'Course'), (5, 'Exercice'), (6, 'Excursion'), (7, 'Presentation'), (8, 'Other'), (9, '')], default=None),
        ),
    ]
