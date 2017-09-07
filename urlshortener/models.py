
from __future__ import unicode_literals
from django.db import models

from .utils import code_genr,create_shortcode

class KirrUrlManager(models.Manager):

	def some_ran(self):
		qs = KirrUrl.objects.all()
		x = qs.count()

		return x
	def refresh_shortcodes(self):
		qs = KirrUrl.objects.all()
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			q.save()
			new_codes+=1
		return "Number of new codes made {}".format(new_codes)




class KirrUrl(models.Model):

	url = models.CharField(max_length=300, )
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	timestamp_updated = models.DateTimeField(auto_now=True)
	timestamp_created = models.DateTimeField(auto_now_add=True)

	objects = KirrUrlManager()
	
	def __str__(self):
		return str(self.url)


	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
			
		super(KirrUrl,self).save(*args, **kwargs)