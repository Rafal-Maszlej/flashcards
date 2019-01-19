from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminUser,)

    @action(methods=['GET'], detail=False, permission_classes=(IsAuthenticated,))
    def my(self, request):
        account = request.user.account
        return Response(self.get_serializer_class()(account).data)
