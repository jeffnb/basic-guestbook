# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from guests.models import Signin


@admin.register(Signin)
class SigninAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')