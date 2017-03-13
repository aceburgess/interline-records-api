from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from django.db import models

# Create your models here.
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class Artist(models.Model):
	display_artist = models.BooleanField(default=False)
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to = 'artist-photos/', null=True, blank=True)
	biography = models.TextField(max_length=500, null=True, blank=True)

	contact_name = models.CharField('Contact / Management Name', max_length=100, default='Interline Records')
	contact_link = models.URLField('Contact / Management URL', default='https://www.interlinerecords.com')
	contact_email = models.EmailField('Contact / Management Email', default='info@interlinerecords.com')

	website = models.URLField(null=True, blank=True)
	spotify = models.URLField(null=True, blank=True)
	youtube = models.URLField('YouTube', null=True, blank=True)
	bandcamp = models.URLField(null=True, blank=True)
	itunes = models.URLField('iTunes', null=True, blank=True)
	facebook = models.URLField(null=True, blank=True)
	twitter = models.URLField(null=True, blank=True)
	instagram = models.URLField(null=True, blank=True)
	soundcloud = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.name


class Album(models.Model):
	title = models.CharField(max_length=100)
	release_date = models.DateField()
	artist = models.ForeignKey(Artist, related_name='albums')

	def __str__(self):
		return self.title

