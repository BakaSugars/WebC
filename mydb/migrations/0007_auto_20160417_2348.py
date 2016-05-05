# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0006_auto_20160417_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_student',
            name='problem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mydb.Problem'),
        ),
        migrations.AlterField(
            model_name='problem_student',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mydb.Student'),
        ),
    ]
