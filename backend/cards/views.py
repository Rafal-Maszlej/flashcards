from rest_framework import viewsets

from cards.models import FlashCardQuestion, FlashCardAnswer, FlashCardCategory
from cards.serializers import FlashCardQuestionSerializer, FlashCardAnswerSerializer, FlashCardCategorySerializer


class FlashCardCategoryViewSet(viewsets.ModelViewSet):
    queryset = FlashCardCategory.objects.all()
    serializer_class = FlashCardCategorySerializer


class FlashCardQuestionViewSet(viewsets.ModelViewSet):
    queryset = FlashCardQuestion.objects.all()
    serializer_class = FlashCardQuestionSerializer


class FlashCardAnswerViewSet(viewsets.ModelViewSet):
    queryset = FlashCardAnswer.objects.all()
    serializer_class = FlashCardAnswerSerializer
