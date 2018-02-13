# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20180123_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'School Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
