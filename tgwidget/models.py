import hashlib
import hmac
import os

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

    def calc_hash(self):
        secret_key = hashlib.sha256(os.getenv('BOT_TOKEN').encode('utf-8')).hexdigest()
        tpl = "auth_date={}\nfirst_name={}\nid={}\nusername={}"
        data_check_string = tpl.format(
            self.tg_auth_date.encode('utf-8'),
            self.tg_first_name.encode('utf-8'),
            self.tg_id.encode('utf-8'),
            self.tg_username.encode('utf-8')
        )
        return hmac.new(secret_key, data_check_string, hashlib.sha256).hexdigest()

    def check_hash(self):
        return self.calc_hash() == self.hash
