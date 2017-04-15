# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(max_length=512)),
                ('score', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
