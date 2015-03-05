from django.db import models

# Create your models here.

class Urls(models.Model):
	long_link = models.URLField(max_length=200)
	short_link = models.URLField(max_length=200, null=True)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.short_link