# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def bookview(request):
    return render(request, 'Book/html.html')
