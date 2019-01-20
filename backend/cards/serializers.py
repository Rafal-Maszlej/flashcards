from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cards.models import Category, CardQuestion, CardAnswer, CardSet


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


class CardSetSerializer(serializers.ModelSerializer):
    size = serializers.CharField(required=False)
    questions = serializers.PrimaryKeyRelatedField(queryset=CardQuestion.objects.all(), many=True)

    class Meta:
        model = CardSet
        fields = '__all__'

    @staticmethod
    def _compute_size(questions):
        len_questions = len(questions)

        for size_key, size_value in settings.CARDS_SET_SIZES.items():
            if len_questions <= size_value:
                return size_key

    @staticmethod
    def _random_questions(number_of_questions):
        return CardQuestion.objects.order_by('?')[:number_of_questions]

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if not (attrs.get('questions') or attrs.get('size')):
            raise ValidationError(f"One of these fields is missing: 'size', 'questions")

        max_questions = max(settings.CARDS_SET_SIZES.values())

        if len(attrs.get('questions')) > max_questions:
            raise ValidationError(f"The maximum number of questions has been exceeded: {max_questions}")

        return attrs

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        data['author'] = self.context['request'].user.account

        return data

    def create(self, validated_data):
        if not validated_data['questions']:
            number_of_questions = settings.CARDS_SET_SIZES[validated_data['size']]

            validated_data['questions'] = self._random_questions(number_of_questions)

        return super().create(validated_data)

    def save(self, **kwargs):
        self.validated_data['size'] = self._compute_size(self.validated_data['questions'])

        return super().save(**kwargs)
