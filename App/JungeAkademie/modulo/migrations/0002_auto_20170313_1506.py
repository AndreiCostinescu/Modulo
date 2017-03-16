# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='interests',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ('title', 'credit', 'time', 'id')},
        ),
        migrations.AlterModelOptions(
            name='testpersons',
            options={'ordering': ('pers_type', 'name')},
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='interests',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='module',
            name='categories',
            field=models.ManyToManyField(to='modulo.Category'),
        ),
        migrations.AddField(
            model_name='module',
            name='credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(default='Empty description..', editable=False),
        ),
        migrations.AddField(
            model_name='module',
            name='exam',
            field=models.IntegerField(choices=[(0, 'Written exam'), (1, 'Oral exam'), (2, 'paper')], default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='place',
            field=models.IntegerField(choices=[(0, 'Freising'), (1, 'Garching'), (2, 'Garching-Hochbrück'), (3, 'Inner city')], default=None),
        ),
        migrations.AddField(
            model_name='module',
            name='time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='module',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='testpersons',
            name='modules',
            field=models.ManyToManyField(to='modulo.Module'),
        ),
        migrations.AddField(
            model_name='testpersons',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='testpersons',
            name='pers_type',
            field=models.IntegerField(choices=[(0, 'strict'), (1, 'loose'), (2, 'curious'), (3, 'credit-oriented'), (4, 'lazy'), (5, 'nerd'), (6, 'do-it-all'), (7, 'time-pressured'), (8, 'detail-oriented'), (9, 'anything works'), (10, 'easy exam'), (11, 'only written exam'), (12, 'the harder, the better')], default=None),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='interests',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='module',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testpersons',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]