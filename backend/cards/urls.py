from rest_framework import routers

from cards.views import FlashCardsViewSet


router = routers.DefaultRouter()
router.register('', FlashCardsViewSet, base_name='card')


urlpatterns = router.urls
