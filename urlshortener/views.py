from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import KirrUrl
# Create your views here.


def home_view(request):

	return render(request,'urlshortener/home.html',{})

def kirr_redirect_view(request, shortcode,):

	obj = get_object_or_404(KirrUrl, shortcode=shortcode)
	return HttpResponseRedirect(obj.url)
