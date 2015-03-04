from django.shortcuts import render
from bitly_api import bitly_api
from .form import SubmitForm
from django.shortcuts import redirect


# Create your views here.

def home(request):

	template = "home.html"
	form = SubmitForm(request.POST or None)
	short_url = None
	if form.is_valid():
		long_url = form.cleaned_data['urlLink']
		short_url = shorten_url(long_url)
		print "short url = %s" % short_url
		return redirect("home")

	
	context = locals()
	return render(request, template, context)

def shorten_url(long_url):
	bitly = bitly_api.Connection('davidnge','R_f5231f7a4063408e81202b9725a6c6fa')
	short_url = bitly.shorten(long_url)['url']
	return short_url

