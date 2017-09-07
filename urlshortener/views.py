# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import KirrUrl
# Create your views here.

def kirr_redirect_view(request, shortcode,):

	obj = get_object_or_404(KirrUrl, shortcode=shortcode)

	return HttpResponse("the url is {sc}".format(sc=obj.url))