from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from cards.views import FlashCardCategoryViewSet, FlashCardQuestionViewSet, FlashCardAnswerViewSet


cards_router = DefaultRouter()
cards_router.register('categories', FlashCardCategoryViewSet, basename='category')

questions_router = routers.NestedDefaultRouter(cards_router, 'categories', lookup='category')
questions_router.register('questions', FlashCardQuestionViewSet, basename='question')

answers_router = routers.NestedDefaultRouter(questions_router, 'questions', lookup='question')
answers_router.register('answers', FlashCardAnswerViewSet, basename='answers')


urlpatterns = cards_router.urls + questions_router.urls + answers_router.urls
