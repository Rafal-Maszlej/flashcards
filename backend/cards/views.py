from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cards.filters import AuthorOrAdminFilter, CardSetFilter
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
    queryset = CardSet.objects.filter()
    serializer_class = CardSetSerializer
    filter_backends = (AuthorOrAdminFilter, filters.DjangoFilterBackend)
    filterset_class = CardSetFilter

    @action(methods=['GET'], detail=False)
    def private(self, request):
        queryset = CardSet.objects.filter(author=request.user.account, public=False)
        return Response(CardSetSerializer(queryset, many=True).data)
