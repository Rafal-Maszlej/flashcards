from django_filters import rest_framework as filters
from rest_framework import viewsets

from cards.filters import AuthorOrAdminFilter, CardSetFilterSet, CardAnswerFilterSet, CardQuestionFilterSet
from cards.models import Category, CardQuestion, CardAnswer, CardSet
from cards.serializers import CategorySerializer, CardQuestionSerializer, CardAnswerSerializer, CardSetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CardQuestionViewSet(viewsets.ModelViewSet):
    queryset = CardQuestion.objects.all()
    serializer_class = CardQuestionSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend,)
    filterset_class = CardQuestionFilterSet


class CardAnswerViewSet(viewsets.ModelViewSet):
    queryset = CardAnswer.objects.all()
    serializer_class = CardAnswerSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend,)
    filterset_class = CardAnswerFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(question=self.kwargs['question_pk'])


class CardSetViewSet(viewsets.ModelViewSet):
    queryset = CardSet.objects.all()
    serializer_class = CardSetSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend)
    filterset_class = CardSetFilterSet
