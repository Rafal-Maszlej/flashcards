from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class FlashCardCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"<Category: {self.name}>"


class FlashCardQuestion(models.Model):
    category = models.ForeignKey(FlashCardCategory, on_delete=models.CASCADE, related_name='questions')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='questions')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Question: {self.category.name}>"


class FlashCardAnswer(models.Model):
    question = models.ForeignKey(FlashCardQuestion, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Answer: {self.question.category.name}>"
