from django.db import models

# Create your models here.

class TgUser(models.Model):
    tg_id = models.CharField(max_length=200, blank=True, null=True,
                             unique=True)
    tg_first_name = models.CharField(max_length=200, blank=True, null=True)
    tg_last_name = models.CharField(max_length=200, blank=True, null=True)
    tg_username = models.CharField(max_length=200, blank=True, null=True)
    tg_photo_url = models.CharField(max_length=200, blank=True, null=True)
    tg_auth_date = models.CharField(max_length=200, blank=True, null=True)
    tg_hash = models.CharField(max_length=200, blank=True, null=True)
