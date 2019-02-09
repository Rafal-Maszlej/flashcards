from django_filters import rest_framework as filters
from rest_framework.filters import BaseFilterBackend

from cards.models import CardSet, CardAnswer, CardQuestion


class AuthorOrAdminFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_staff:
            return queryset
        return queryset.filter(author=request.user.account)


class CardSetFilter(filters.FilterSet):
    class Meta:
        model = CardSet
        fields = ('public', 'size', 'category')


class CardAnswerFilter(filters.FilterSet):
    class Meta:
        model = CardAnswer
        fields = ('correct',)


class CardQuestionFilter(filters.FilterSet):
    class Meta:
        model = CardQuestion
        fields = ('public', 'category')
