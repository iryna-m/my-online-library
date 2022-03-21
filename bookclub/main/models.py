from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255),
    description = models.TextField(blank=True),
    cover = models.ImageField(upload_to='covers/'),
    is_published = models.BooleanField(default=True)