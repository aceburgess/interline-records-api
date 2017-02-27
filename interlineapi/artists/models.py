from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from django.db import models

# Create your models here.
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class Artist(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to = 'artist-photos/', blank=True)
	biography = models.TextField(max_length=500, blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.name


class Album(models.Model):
	title = models.CharField(max_length=100)
	release_date = models.DateField()
	artist = models.ForeignKey(Artist, related_name='albums')

	def __str__(self):
		return self.title

