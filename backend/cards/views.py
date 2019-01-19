from rest_framework import viewsets

from cards.models import Category, CardQuestion, CardAnswer, CardSet
from cards.serializers import CategorySerializer, CardQuestionSerializer, CardAnswerSerializer, CardSetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CardQuestionViewSet(viewsets.ModelViewSet):
    queryset = CardQuestion.objects.all()
    serializer_class = CardQuestionSerializer


class CardAnswerViewSet(viewsets.ModelViewSet):
    queryset = CardAnswer.objects.all()
    serializer_class = CardAnswerSerializer


class CardSetViewSet(viewsets.ModelViewSet):
    queryset = CardSet.objects.all()
    serializer_class = CardSetSerializer
