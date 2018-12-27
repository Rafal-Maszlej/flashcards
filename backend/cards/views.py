from rest_framework import viewsets

from cards.models import FlashCardQuestion
from cards.serializers import FlashCardQuestionSerializer


class FlashCardQuestionViewSet(viewsets.ModelViewSet):
    queryset = FlashCardQuestion.objects.all()
    serializer_class = FlashCardQuestionSerializer
