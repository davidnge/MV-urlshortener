from django.db import models

# Create your models here.

class Urls(models.Model):
	urlLink = models.URLField(max_length=200)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.urlLink