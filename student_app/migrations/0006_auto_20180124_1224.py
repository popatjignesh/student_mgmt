# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_auto_20180124_0510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='School',
            new_name='school',
        ),
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='contact_no',
            field=models.BigIntegerField(max_length=13, null=True, verbose_name=b'Contact No.', blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='rating',
            field=models.CharField(max_length=10, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
        ),
        migrations.AlterField(
            model_name='school',
            name='website',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fees',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='residental_address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(max_length=10, choices=[(b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')]),
        ),
    ]
