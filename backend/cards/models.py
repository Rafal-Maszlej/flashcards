from django.db import models

from accounts.models import Account


class CardCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"<Category: {self.name}>"


class CardQuestion(models.Model):
    category = models.ForeignKey(CardCategory, on_delete=models.CASCADE, related_name='questions')
    author = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL, related_name='questions')
    content = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Question: {self.content}>"


class CardAnswer(models.Model):
    question = models.ForeignKey(CardQuestion, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='answers')
    content = models.CharField(max_length=200)
    correct = models.NullBooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Answer: {self.question.content}>"