from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from cards.views import CategoryViewSet, CardQuestionViewSet, CardAnswerViewSet


cards_router = DefaultRouter()
cards_router.register('categories', CategoryViewSet, basename='category')

questions_router = NestedDefaultRouter(cards_router, 'categories', lookup='category')
questions_router.register('questions', CardQuestionViewSet, basename='question')

answers_router = NestedDefaultRouter(questions_router, 'questions', lookup='question')
answers_router.register('answers', CardAnswerViewSet, basename='answers')


urlpatterns = cards_router.urls + questions_router.urls + answers_router.urls
