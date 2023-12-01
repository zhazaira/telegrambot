from django.db import models


class Programming(models.Model):
    language= models.CharField(max_length=255)
    since = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title