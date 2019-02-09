from django.urls import reverse
from rest_framework import status, test

from accounts.models import Account
from accounts.tests.factories import AccountFactory


class AccountsListTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.accounts_list_url = reverse('accounts-list')

        cls.admin_account = AccountFactory(user__is_staff=True)
        cls.non_admin_account = AccountFactory()

    def test_unauthenticated_user_cannot_get_accounts_list(self):
        response = self.client.get(self.accounts_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_admin_cannot_get_accounts_list(self):
        self.client.force_login(self.non_admin_account.user)

        response = self.client.get(self.accounts_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_get_accounts_list(self):
        self.client.force_login(self.admin_account.user)

        response = self.client.get(self.accounts_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Account.objects.count())


class AccountMyTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.accounts_my_url = reverse('accounts-me')

        cls.account1 = AccountFactory()
        cls.account2 = AccountFactory()

    def setUp(self):
        self.client.force_login(self.account1.user)

    def test_user_retrieve_own_account_details(self):
        response = self.client.get(self.accounts_my_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user'], self.account1.pk)
