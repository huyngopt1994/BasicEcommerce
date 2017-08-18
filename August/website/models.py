from __future__ import unicode_literals

from django.db import models

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    localtion = models.TextField(null=True)
    contact = models.CharField(max_length=100, default="None")

    def __str__(self):
        return unicode(self.name).encode('utf-8')