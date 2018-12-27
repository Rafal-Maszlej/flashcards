from rest_framework import routers

from cards.views import FlashCardQuestionViewSet


router = routers.DefaultRouter()
router.register('', FlashCardQuestionViewSet, base_name='card')


urlpatterns = router.urls
