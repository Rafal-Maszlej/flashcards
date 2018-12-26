from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class FlashCardCategory(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return f"<Category: {self.title}>"


class FlashCard(models.Model):
    title = models.CharField(max_length=120)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)

    category = models.ForeignKey(FlashCardCategory, on_delete=models.CASCADE, related_name='cards')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='cards')

    def __str__(self):
        return f"<Card {self.title} - {self.category}>"
