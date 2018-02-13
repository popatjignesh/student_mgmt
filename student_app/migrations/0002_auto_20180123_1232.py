# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('residental_address', models.TextField(blank=True)),
                ('standard', models.CharField(max_length=10, null=True, choices=[(b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('roll_no', models.IntegerField(blank=True)),
                ('fees', models.IntegerField(blank=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('School', models.ForeignKey(to='student_app.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='school',
            name='contact_no',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
