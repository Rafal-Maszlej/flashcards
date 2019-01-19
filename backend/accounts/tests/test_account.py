from django.urls import reverse
from rest_framework import status, test

from accounts.models import Account
from accounts.tests.factories import AccountFactory


class AccountsListTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.account_list_url = reverse('accounts-list')

        cls.admin_account = AccountFactory(user__is_staff=True)
        cls.non_admin_account = AccountFactory()

    def test_unauthenticated_user_cannot_get_accounts_list(self):
        response = self.client.get(self.account_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_admin_cannot_get_accounts_list(self):
        self.client.force_login(self.non_admin_account.user)

        response = self.client.get(self.account_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_get_accounts_list(self):
        self.client.force_login(self.admin_account.user)

        response = self.client.get(self.account_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Account.objects.count())
