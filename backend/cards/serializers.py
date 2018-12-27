from rest_framework import serializers

from cards.models import FlashCardQuestion, FlashCardAnswer, FlashCardCategory


class FlashCardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCardCategory
        fields = '__all__'


class FlashCardQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCardQuestion
        fields = '__all__'


class FlashCardAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCardAnswer
        fields = '__all__'
