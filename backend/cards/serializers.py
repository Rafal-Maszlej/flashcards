from rest_framework import serializers

from cards.models import FlashCardQuestion


class FlashCardQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCardQuestion
        fields = '__all__'
