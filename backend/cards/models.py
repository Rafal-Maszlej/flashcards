from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class FlashCardsGroup(models.Model):
    title = models.CharField(max_length=120)


class FlashCard(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(FlashCardsGroup, on_delete=models.CASCADE, related_name='category')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='author')
