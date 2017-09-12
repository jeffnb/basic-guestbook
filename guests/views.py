# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render

from guests.forms import SigninForm
from guests.models import Signin


def list_signins(request):


    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/")

    else:
        form = SigninForm()

    signins = Signin.objects.all().order_by('-created')

    return render(request, "guests/index.html", {'signins': signins, 'form': form})
