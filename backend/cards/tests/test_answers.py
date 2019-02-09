from django.urls import reverse
from rest_framework import status, test

from accounts.tests.factories import AccountFactory
from cards.tests.factories import CardAnswerFactory, CardQuestionFactory


class CardAnswerListTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = CardQuestionFactory()
        cls.answer_list_url = reverse('answer-list', args=(cls.question.pk,))

        cls.account = AccountFactory()
        cls.admin_account = AccountFactory(user__is_staff=True)

        cls.answer = CardAnswerFactory(author=cls.account, question=cls.question)
        cls.other_answer = CardAnswerFactory(question=cls.question)

        cls.answer_other_question = CardAnswerFactory(author=cls.account)

    def setUp(self):
        self.client.force_login(self.account.user)

    def test_unauthenticated_user_cannot_access(self):
        self.client.logout()

        response = self.client.get(self.answer_list_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_get_all_answers_from_one_question(self):
        self.client.force_login(self.admin_account.user)

        response = self.client.get(self.answer_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertNotIn(self.answer_other_question.pk, [answer['id'] for answer in response.data])

    def test_user_get_own_answers_from_one_question(self):
        response = self.client.get(self.answer_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.answer.pk)

    def test_get_answers_wrong_question(self):
        wrong_url = reverse('answer-list', args=(0,))
        response = self.client.get(wrong_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
