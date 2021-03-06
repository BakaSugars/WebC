# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.IntegerField()),
                ('e_name', models.TextField()),
                ('e_point', models.IntegerField()),
                ('contain', models.TextField()),
                ('output', models.TextField()),
                ('dif', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('problem_id', models.IntegerField()),
                ('problem_student_code', models.TextField()),
                ('problem_student_review', models.TextField()),
                ('problem_student_condition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SmallTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('student_name', models.CharField(max_length=50)),
                ('student_teacherid', models.CharField(max_length=50)),
                ('student_teachername', models.CharField(max_length=30)),
                ('student_class', models.CharField(max_length=30)),
                ('studnet_grade', models.CharField(max_length=30)),
                ('student_point', models.IntegerField()),
                ('student_rank', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('teacher_password', models.CharField(max_length=30)),
            ],
        ),
    ]
