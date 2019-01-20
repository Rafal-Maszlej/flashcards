from django.urls import reverse
from rest_framework import status, test

from accounts.tests.factories import AccountFactory
from cards.tests.factories import CardSetFactory


class CardSetListTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.card_set_list_url = reverse('card-set-list')

        cls.account = AccountFactory()
        cls.admin_account = AccountFactory(user__is_staff=True)

        cls.admin_card_set = CardSetFactory(author=cls.admin_account, public=True)
        cls.card_set_public = CardSetFactory(author=cls.account, public=True)
        cls.card_set_private = CardSetFactory(author=cls.account, public=False)
        cls.other_card_set = CardSetFactory(public=True)

    def setUp(self):
        self.client.force_login(self.account.user)

    def test_unauthenticated_user_cannot_access(self):
        self.client.logout()

        response = self.client.get(self.card_set_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_get_all_public_sets(self):
        self.client.force_login(self.admin_account.user)

        response = self.client.get(self.card_set_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertNotIn(self.card_set_private.pk, [card_set['id'] for card_set in response.data])

    def test_user_get_own_public_sets(self):
        response = self.client.get(self.card_set_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.card_set_public.pk)
