# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=256, blank=False)
    link = models.CharField(max_length=512, blank=False)
    score = models.IntegerField(default=1)
