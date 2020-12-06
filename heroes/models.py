from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]
