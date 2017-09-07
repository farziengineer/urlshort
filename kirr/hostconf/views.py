from django.http import HttpResponseRedirect, HttpResponse

def wildcard_redirect(request, path):
	return HttpResponse("the requested subdomain is {sub}".format(sub=path))
