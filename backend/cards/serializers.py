from rest_framework import serializers

from cards.models import CardQuestion, CardAnswer, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CardQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardQuestion
        fields = '__all__'


class CardAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardAnswer
        fields = '__all__'
