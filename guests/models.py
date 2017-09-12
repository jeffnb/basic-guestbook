# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Signin(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

