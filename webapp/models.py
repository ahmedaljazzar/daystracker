# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Happiness(models.Model):
    score = models.PositiveSmallIntegerField()
    date = models.DateField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Productivity(models.Model):
    score = models.PositiveSmallIntegerField()
    date = models.DateField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Learning(models.Model):
    score = models.PositiveSmallIntegerField()
    date = models.DateField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
