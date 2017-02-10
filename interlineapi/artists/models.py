from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to = 'artist-photos/', blank=True)
	biography = models.TextField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.name


class Album(models.Model):
	title = models.CharField(max_length=100)
	release_date = models.DateField()
	artist = models.ForeignKey(Artist, related_name='albums')

	def __str__(self):
		return self.title