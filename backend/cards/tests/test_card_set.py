from django.test import override_settings
from django.urls import reverse
from rest_framework import status, test

from accounts.tests.factories import AccountFactory
from cards.tests.config import CARDSET_SIZES
from cards.tests.factories import CategoryFactory, CardSetFactory, CardQuestionFactory


class CardSetListTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cardset_list_url = reverse('cardset-list')

        cls.account = AccountFactory()
        cls.admin_account = AccountFactory(user__is_staff=True)

        cls.cardset_public = CardSetFactory(author=cls.account, public=True)
        cls.cardset_private = CardSetFactory(author=cls.account, public=False)
        cls.admin_cardset = CardSetFactory(author=cls.admin_account, public=True)
        cls.other_cardset_public = CardSetFactory(public=True)
        cls.other_cardset_private = CardSetFactory(public=False)

    def setUp(self):
        self.client.force_login(self.account.user)

    def test_unauthenticated_user_cannot_access(self):
        self.client.logout()

        response = self.client.get(self.cardset_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_get_all_sets(self):
        self.client.force_login(self.admin_account.user)

        response = self.client.get(self.cardset_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_user_get_own_sets(self):
        response = self.client.get(self.cardset_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        response_cardset_pks = [cardset['id'] for cardset in response.data]

        self.assertIn(self.cardset_public.pk, response_cardset_pks)
        self.assertIn(self.cardset_private.pk, response_cardset_pks)


@override_settings(CARDSET_SIZES=CARDSET_SIZES)
class CreateCardSetTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cardset_list_url = reverse('cardset-list')

        cls.account = AccountFactory()
        cls.category = CategoryFactory()
        cls.questions = CardQuestionFactory.create_batch(10, author=None)

    def setUp(self):
        self.size = 'M'
        self.questions_pk = [question.pk for question in self.questions[:CARDSET_SIZES[self.size]]]
        self.data = {
            'title': 'test title',
            'description': 'test description',
            'public': True,
            'category': self.category.pk,
            'questions': self.questions_pk
        }

        self.client.force_login(self.account.user)

    def test_create_cardset_common_fields(self):
        response = self.client.post(self.cardset_list_url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('title'), self.data['title'])
        self.assertEqual(response.data.get('description'), self.data['description'])
        self.assertTrue(response.data.get('public'))
        self.assertEqual(response.data.get('category'), self.data['category'])
        self.assertListEqual(response.data.get('questions'), self.questions_pk)

    def test_correct_author(self):
        response = self.client.post(self.cardset_list_url, data=self.data)

        self.assertEqual(response.data.get('author'), self.account.pk)

    def test_compute_cardset_size_field(self):
        response = self.client.post(self.cardset_list_url, data=self.data)

        self.assertEqual(response.data.get('size'), self.size)

    def test_random_questions_based_on_size(self):
        self.data['questions'] = []
        self.data['size'] = list(CARDSET_SIZES.keys())[0]

        response = self.client.post(self.cardset_list_url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data['questions']), CARDSET_SIZES[self.data['size']])

    def test_cannot_create_cardset_without_both_size_and_questions(self):
        self.data['questions'] = []

        response = self.client.post(self.cardset_list_url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_add_more_questions_than_max_size(self):
        self.data['questions'] = [question.pk for question in self.questions]

        response = self.client.post(self.cardset_list_url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
