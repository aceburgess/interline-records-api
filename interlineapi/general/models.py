from __future__ import unicode_literals
from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class SiteSetting(models.Model):
	site_title = models.CharField(max_length=100, blank=True)
	site_description = models.CharField(max_length=250, blank=True)
	facebook = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	youtube = models.URLField(blank=True)
	store = models.URLField(blank=True)

	about_us = models.TextField(max_length=600, blank=True)
	contact = models.TextField(max_length=600, blank=True)
	contact_photo = models.ImageField('Conatct Photo', upload_to = 'site-photos/', blank=True)
	contact_name = models.CharField(max_length=100, blank=True)
	contact_email = models.EmailField(max_length=200, blank=True)

	background_photo_lp = models.ImageField('Background Photo Landing Page', upload_to = 'site-photos/', blank=True)
	background_photo_ap = models.ImageField('Background Photo Artist Page', upload_to = 'site-photos/', blank=True)
	background_photo_ad = models.ImageField('Background Photo Artist Detail Page', upload_to = 'site-photos/', blank=True)


	def save(self, *args, **kwargs):
		if SiteSetting.objects.exists() and not self.pk:
			raise ValidationError('There can only be one SiteSettings instance')

		return super(SiteSetting, self).save(*args, **kwargs)

	def __str__(self):
		return self.site_title + ' Site Settings'

class Announcement(models.Model):
	announcement = models.TextField(max_length=300, blank=True)
	link = models.URLField(blank=True)
	public_date = models.DateTimeField()


	def __str__(self):
		return self.announcement



