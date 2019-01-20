from django.db import models


class PublicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(public=True)


class PrivateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(public=False)
