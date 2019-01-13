from rest_framework import viewsets

from cards.models import CardQuestion, CardAnswer, CardCategory
from cards.serializers import CardQuestionSerializer, CardAnswerSerializer, CardCategorySerializer


class CardCategoryViewSet(viewsets.ModelViewSet):
    queryset = CardCategory.objects.all()
    serializer_class = CardCategorySerializer


class CardQuestionViewSet(viewsets.ModelViewSet):
    queryset = CardQuestion.objects.all()
    serializer_class = CardQuestionSerializer


class CardAnswerViewSet(viewsets.ModelViewSet):
    queryset = CardAnswer.objects.all()
    serializer_class = CardAnswerSerializer
