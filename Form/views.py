# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def FormView(request):
    return render(request, 'Form/html.html')
