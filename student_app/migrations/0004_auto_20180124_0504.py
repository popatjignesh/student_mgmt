# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_auto_20180124_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
