# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0008_auto_20180124_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=25),
        ),
    ]
