# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True)),
                ('rating', models.CharField(max_length=10, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
                ('email', models.EmailField(max_length=75)),
                ('contact_no', models.DecimalField(max_digits=13, decimal_places=10, blank=True)),
                ('website', models.CharField(max_length=50, blank=True)),
                ('enabled', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
