from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Album(models.Model):
	title = models.CharField(max_length=100)
	release_date = models.DateField()
	artist = models.ForeignKey(Artist, related_name='albums')

	def __str__(self):
		return self.title