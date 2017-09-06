# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class KirrUrl(models.Model):
	url = models.CharField(max_length=300, )
	shortcode = models.CharField(max_length=15, unique=True)
	timestamp_updated = models.DateTimeField(auto_now=True)
	timestamp_created = models.DateTimeField(auto_now_add=True )	
	def __str__(self):
		return str(self.url)
