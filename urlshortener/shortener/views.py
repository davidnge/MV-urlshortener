from django.shortcuts import render
from bitly_api import bitly_api
from .form import SubmitForm
from django.shortcuts import redirect
from .models import Urls
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings



# Create your views here.

def home(request):

	template = "home.html"
	form = SubmitForm(request.POST or None)
	link_list = Urls.objects.all()
	short_url = None
	just_shorten_link = None #most recent link shortened
	prev_links = None #previous shortened links except for most recent
	paginator = None

	if form.is_valid():
		long_url = form.cleaned_data['urlLink']
		short_url = shorten_url(long_url)
		new_link = Urls.objects.create(long_link=long_url, short_link=short_url)  
		new_link.save()
		return redirect("home")

	if link_list.count() > 0:
		just_shorten_link = link_list.last()
	if link_list.count() > 1:
		prev_links = reversed(link_list.reverse()[:link_list.count()-1])

	context = locals()
	return render(request, template, context)

#calling bitly api
def shorten_url(long_url):
	bitly = bitly_api.Connection(settings.BITLY_USER,settings.BITLY_API_KEY)
	short_url = bitly.shorten(long_url)['url']
	return short_url

