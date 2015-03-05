from django.contrib import admin
from .models import Urls

# Register your models here.

class UrlsAdmin(admin.ModelAdmin):
	urls_list = ('urlLink', 'pub_date')
	ordering = ('-pub_date',)

admin.site.register(Urls, UrlsAdmin)