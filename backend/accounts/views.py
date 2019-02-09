from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    list:
        Get list of all accounts. (Admin only)

    retrieve:
        Get account details. (Admin only)

    create:
        Create an account. (Admin only)

    partial_update:
        Update one or more account fields. (Admin only)

    update:
        Update a account. (Admin only)

    delete:
        Delete an account. (Admin only)

    me:
        Get logged-in user account details.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminUser,)

    @action(methods=['GET'], detail=False, permission_classes=(IsAuthenticated,))
    def me(self, request):
        account = request.user.account
        return Response(self.get_serializer_class()(account).data)
