from django.conf import settings
from django.db import models
from django.utils import timezone

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addr = models.TextField()

    def __str__(self):
        return self.addr
