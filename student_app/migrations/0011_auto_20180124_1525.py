# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0010_auto_20180124_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': 'School', 'verbose_name_plural': 'School'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Student'},
        ),
    ]
