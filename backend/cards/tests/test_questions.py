from django.urls import reverse
from rest_framework import status, test

from accounts.tests.factories import AccountFactory
from cards.tests.factories import CardQuestionFactory


class CardQuestionListTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question_list_url = reverse('question-list')

        cls.account = AccountFactory()
        cls.admin_account = AccountFactory(user__is_staff=True)

        cls.question_public = CardQuestionFactory(author=cls.account, public=True)
        cls.question_private = CardQuestionFactory(author=cls.account, public=False)
        cls.admin_question_public = CardQuestionFactory(author=cls.admin_account, public=True)
        cls.other_question_public = CardQuestionFactory(public=True)
        cls.other_question_private = CardQuestionFactory(public=False)

    def setUp(self):
        self.client.force_login(self.account.user)

    def test_unauthenticated_user_cannot_access(self):
        self.client.logout()

        response = self.client.get(self.question_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_get_all_questions(self):
        self.client.force_login(self.admin_account.user)

        response = self.client.get(self.question_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_user_get_own_questions(self):
        response = self.client.get(self.question_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        response_question_pks = [question['id'] for question in response.data]

        self.assertIn(self.question_public.pk, response_question_pks)
        self.assertIn(self.question_private.pk, response_question_pks)
