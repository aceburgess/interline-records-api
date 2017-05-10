from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from django.db import models
from datetime import datetime

# Create your models here.
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class Artist(models.Model):
	display = models.BooleanField('DISPLAY ARTIST PUBLICLY ?', default=False)
	name = models.CharField(max_length=100)
	slug = models.SlugField(null=True)
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
	vimeo = models.URLField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	def __str__(self):
		return self.name


class Album(models.Model):
	display = models.BooleanField('PUBLIC ?', default=True)
	title = models.CharField(max_length=100)
	link = models.URLField()
	cover_art = models.ImageField(upload_to = 'cover-art-photos/', null=True, blank=True)
	release_date = models.DateField(default=datetime.now, blank=True)
	label = models.CharField(max_length=150, default='Interline Records')
	artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	def __str__(self):
		return self.title

class Video(models.Model):
	VIDEO_CHOICES = (
		('yt', 'Youtube'),
		('vm', 'Vimeo'),
	)

	display = models.BooleanField('PUBLIC ?', default=True)
	title = models.CharField(max_length=100)
	link = models.URLField()
	description = models.CharField(max_length=200, null=True, blank=True)
	release_date = models.DateField(default=datetime.now, blank=True)
	video_service = models.CharField(max_length=2, choices=VIDEO_CHOICES, default='yt')
	artist = models.ForeignKey(Artist, related_name='videos', on_delete=models.CASCADE)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	def __str__(self):
		return self.title









