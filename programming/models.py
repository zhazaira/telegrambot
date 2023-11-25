from django.db import models


class Programming(models.Model):
    language= models.CharField(max_length=255)
    since = models.IntegerField()
