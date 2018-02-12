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
#    tg_hash = models.CharField(max_length=200, blank=True, null=True)

    @staticmethod
    def make_from_dict(data):
        user, created = TgUser.objects.get_or_create(tg_id=data.get('id', ''))
        user.tg_first_name = data.get('first_name', '')
        user.tg_last_name = data.get('last_name', '')
        user.tg_username = data.get('username', '')
        user.tg_photo_url = data.get('photo_url', '')
        user.tg_auth_date = data.get('auth_date', '')
 #       user.tg_hash = data.get('hash', '')
        return user
