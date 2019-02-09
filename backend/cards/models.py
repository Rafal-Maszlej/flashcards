from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from accounts.models import Account


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"<Category: {self.name}>"


class CardQuestion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    author = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL, related_name='questions')
    content = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
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


class CardSet(models.Model):
    class SizeType(DjangoChoices):
        small = ChoiceItem("S")
        medium = ChoiceItem("M")
        large = ChoiceItem("L")

    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='card_sets')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='card_sets')
    questions = models.ManyToManyField(CardQuestion)
    size = models.CharField(max_length=1, choices=SizeType.choices)
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<CardSet: {self.pk}>"
