from django.urls import reverse
from rest_framework import status, test

from accounts.tests.factories import AccountFactory
from cards.models import CardAnswer
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


class SubmitAnswerTestCase(test.APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = CardQuestionFactory()
        cls.answer_list_url = reverse('answer-list', args=(cls.question.pk,))
        cls.account = AccountFactory()

    def setUp(self):
        self.answer_data = {
            "content": self.question.correct_answer
        }
        self.client.force_login(self.account.user)

    def test_correct_data(self):
        response = self.client.post(self.answer_list_url, data=self.answer_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CardAnswer.objects.exists())

    def test_correct_author(self):
        response = self.client.post(self.answer_list_url, data=self.answer_data)

        self.assertEqual(response.data.get('author'), self.account.pk)

    def test_correct_question(self):
        response = self.client.post(self.answer_list_url, data=self.answer_data)

        self.assertEqual(response.data.get('question'), self.question.pk)

    def test_wrong_answer(self):
        self.answer_data['content'] = 'wrong answer'

        response = self.client.post(self.answer_list_url, data=self.answer_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data.get('correct'))

    def test_correct_answer(self):
        response = self.client.post(self.answer_list_url, data=self.answer_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get('correct'))

    def test_question_does_not_exist(self):
        wrong_question = reverse('answer-list', args=(self.question.pk + 1,))

        response = self.client.post(wrong_question, self.answer_data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
