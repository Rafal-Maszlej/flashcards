from rest_framework.routers import DefaultRouter

from accounts.views import AccountViewSet


accounts_router = DefaultRouter()
accounts_router.register('', AccountViewSet, basename='accounts')

urlpatterns = accounts_router.urls
