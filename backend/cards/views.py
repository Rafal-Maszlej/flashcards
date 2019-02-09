from django_filters import rest_framework as filters
from rest_framework import viewsets

from cards.filters import AuthorOrAdminFilter, CardSetFilterSet, CardAnswerFilterSet, CardQuestionFilterSet
from cards.models import Category, CardQuestion, CardAnswer, CardSet
from cards.serializers import CategorySerializer, CardQuestionSerializer, CardAnswerSerializer, CardSetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    list:
        Get list of all categories.

    retrieve:
        Get category details.

    create:
        Create a category.

    partial_update:
        Update one or more category fields.

    update:
        Update a category.

    delete:
        Delete a category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CardQuestionViewSet(viewsets.ModelViewSet):
    """
    list:
        Get list of all questions.

    retrieve:
        Get question details.

    create:
        Create a question.

    partial_update:
        Update one or more question fields.

    update:
        Update a question.

    delete:
        Delete a question.
    """
    queryset = CardQuestion.objects.all()
    serializer_class = CardQuestionSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend,)
    filterset_class = CardQuestionFilterSet


class CardAnswerViewSet(viewsets.ModelViewSet):
    """
    list:
        Get list of answers from specified question.

    retrieve:
        Get answer details.

    create:
        Submit an answer.

    delete:
        Delete a category.
    """
    queryset = CardAnswer.objects.all()
    serializer_class = CardAnswerSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend,)
    filterset_class = CardAnswerFilterSet
    http_method_names = ('get', 'post', 'delete')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(question=self.kwargs['question_pk'])


class CardSetViewSet(viewsets.ModelViewSet):
    """
    list:
        Get list of all card sets.

    retrieve:
        Get card set details.

    create:
        Create a card set.

    partial_update:
        Update one or more card set fields.

    update:
        Update a card set.

    delete:
        Delete a card set.
    """
    queryset = CardSet.objects.all()
    serializer_class = CardSetSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend)
    filterset_class = CardSetFilterSet
