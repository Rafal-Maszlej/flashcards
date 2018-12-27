from rest_framework import routers

from cards.views import FlashCardCategoryViewSet


router = routers.DefaultRouter()
router.register('categories', FlashCardCategoryViewSet, base_name='category')


urlpatterns = router.urls
