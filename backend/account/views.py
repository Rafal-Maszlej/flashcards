from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from account.models import Account
from account.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminUser,)
