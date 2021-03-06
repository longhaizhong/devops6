# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlmng', '0003_auto_20180314_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sqlconf',
            name='backid',
        ),
        migrations.AddField(
            model_name='sqlconf',
            name='commiter',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sqlconf',
            name='dbname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='sqlconf',
            name='rollbackopid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sqlconf',
            name='backdb',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sqlconf',
            name='condtion',
            field=models.IntegerField(choices=[(-3, '\u5df2\u56de\u6eda'), (-2, '\u5df2\u6682\u505c'), (-1, '\u5f85\u6267\u884c'), (0, '\u5df2\u6267\u884c'), (1, '\u5df2\u653e\u5f03'), (2, '\u6267\u884c\u5931\u8d25')], default=-1),
        ),
        migrations.AlterField(
            model_name='sqlconf',
            name='sqlcontent',
            field=models.TextField(blank=True, null=True),
        ),
    ]
