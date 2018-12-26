from rest_framework import viewsets

from cards.models import FlashCard
from cards.serializers import FlashCardSerializer


class FlashCardsViewSet(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
