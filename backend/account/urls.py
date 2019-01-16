from rest_framework.routers import DefaultRouter

from account.views import AccountViewSet


account_router = DefaultRouter()
account_router.register('', AccountViewSet, basename='accounts')

urlpatterns = account_router.urls
