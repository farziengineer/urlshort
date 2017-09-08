from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import KirrUrl
from .forms import SubmitUrlForm

def home_view(request):
	title = "Tirr.co"
	if request.method == "POST":
		the_form = SubmitUrlForm(request.POST)
		if the_form.is_valid():
			print (the_form.cleaned_data)
		context = {
			"form": the_form,
			"title": title,
		}
		
		return render(request, 'urlshortener/home.html', context)			


	the_form = SubmitUrlForm()
	context = {
		"form": the_form,
		"title": title,
	}
	return render(request,'urlshortener/home.html',context)

def kirr_redirect_view(request, shortcode,):

	obj = get_object_or_404(KirrUrl, shortcode=shortcode)
	return HttpResponseRedirect(obj.url)
