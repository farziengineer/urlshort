from django.core.management.base import BaseCommand, CommandError

from urlshortener.models import KirrUrl

class Command(BaseCommand):
	help = 'Refreshes all KirrUrl shortcodes'
	
	def handle(self, *args, **kwargs):
		return KirrUrl.objects.refresh_shortcodes()

