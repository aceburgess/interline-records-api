from __future__ import unicode_literals
from django.core.exceptions import ValidationError

from django.db import models
from interlineapi.artists.models import Artist, Album, Video

# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Staff(models.Model):
	display = models.BooleanField('DISPLAY STAFF MEMBER PUBLICLY ?', default=False)
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	job_title = models.CharField(max_length=120, blank=True)
	email = models.EmailField(max_length=200, blank=True)
	description = models.CharField(max_length=250, blank=True)
	photo = models.ImageField(upload_to = 'staff-photos/', null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		verbose_name='Staff'
		verbose_name_plural='Staff'

	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' - ' + self.job_title

class Company(models.Model):
	display = models.BooleanField('DISPLAY COMPANY PUBLICLY ?', default=False)
	name = models.CharField(max_length=100, blank=True)
	business_type = models.CharField('Type of Compnay', max_length=120, blank=True)
	email = models.EmailField(max_length=200, blank=True)
	website = models.URLField(blank=True)
	description = models.CharField(max_length=250, blank=True)
	photo = models.ImageField(upload_to = 'staff-photos/', null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		verbose_name='Companies We Work With'
		verbose_name_plural='Companies We Work With'

	def __str__(self):
		return self.name + ' - ' + self.duty


class SiteSetting(models.Model):
	site_title = models.CharField(max_length=100, blank=True)
	site_description = models.CharField(max_length=250, blank=True)

	facebook = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	youtube = models.URLField(blank=True)
	store = models.URLField(blank=True)

	about_us = models.TextField(max_length=600, blank=True)
	contact_name = models.CharField(max_length=100, blank=True)
	contact_email = models.EmailField(max_length=200, blank=True)

	background_photo_lp = models.ImageField('Background Photo Landing Page', upload_to = 'site-photos/', blank=True)
	background_photo_mc = models.ImageField('Background Photo Artist Page', upload_to = 'site-photos/', blank=True)
	background_photo_ad = models.ImageField('Background Photo Artist Detail Page', upload_to = 'site-photos/', blank=True)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		verbose_name='Site Settings'
		verbose_name_plural='Site Settings'

	def save(self, *args, **kwargs):
		if SiteSetting.objects.exists() and not self.pk:
			raise ValidationError('There can only be one SiteSettings instance')

		return super(SiteSetting, self).save(*args, **kwargs)

	def __str__(self):
		return self.site_title + ' Site Settings'

class Announcement(models.Model):
	display = models.BooleanField('PUBLIC ?', default=False)
	announcement = models.CharField(max_length=250, blank=True)
	link = models.URLField(blank=True)
	artist = models.ForeignKey(Artist, related_name='announcements', on_delete=models.CASCADE, null=True, blank=True)
	album = models.ForeignKey(Album, related_name='announcements', on_delete=models.CASCADE, null=True, blank=True)
	video = models.ForeignKey(Video, related_name='announcements', on_delete=models.CASCADE, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	def __str__(self):
		return self.announcement

class MailingList(models.Model):
	email = models.URLField()
	name = models.CharField(max_length=200, blank=True, null=True)
	ip_address = models.GenericIPAddressField(blank=True, null=True)
	city = models.CharField(max_length=200, null=True, blank=True)
	region = models.CharField(max_length=200, null=True, blank=True)
	country = models.CharField(max_length=200, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)


