from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cards.filters import AuthorOrAdminFilter, CardSetFilter, CardQuestionFilter
from cards.models import Category, CardQuestion, CardAnswer, CardSet
from cards.serializers import CategorySerializer, CardQuestionSerializer, CardAnswerSerializer, CardSetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CardQuestionViewSet(viewsets.ModelViewSet):
    queryset = CardQuestion.objects.all()
    serializer_class = CardQuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CardQuestionFilter


class CardAnswerViewSet(viewsets.ModelViewSet):
    queryset = CardAnswer.objects.all()
    serializer_class = CardAnswerSerializer


class CardSetViewSet(viewsets.ModelViewSet):
    queryset = CardSet.objects.filter()
    serializer_class = CardSetSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend)
    filterset_class = CardSetFilter
