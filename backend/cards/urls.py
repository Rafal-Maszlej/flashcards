from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from cards.views import CategoryViewSet, CardQuestionViewSet, CardAnswerViewSet, CardSetViewSet


cards_router = DefaultRouter()
cards_router.register('categories', CategoryViewSet, basename='category')
cards_router.register('questions', CardQuestionViewSet, basename='question')
cards_router.register('', CardSetViewSet, basename='card-set')

answers_router = NestedDefaultRouter(cards_router, 'questions', lookup='question')
answers_router.register('answers', CardAnswerViewSet, basename='answers')


urlpatterns = cards_router.urls + answers_router.urls
