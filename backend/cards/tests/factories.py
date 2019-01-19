import factory
from factory import fuzzy

from accounts.tests.factories import AccountFactory
from cards.models import Category, CardQuestion, CardAnswer, CardSet


class CategoryFactory(factory.DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Category


class CardQuestionFactory(factory.DjangoModelFactory):
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(AccountFactory)
    content = factory.Faker('sentence')
    correct_answer = factory.Faker('sentence')
    created_at = factory.Faker('date_this_decade', before_today=True)

    class Meta:
        model = CardQuestion


class CardAnswerFactory(factory.DjangoModelFactory):
    question = factory.SubFactory(CardQuestionFactory)
    author = factory.SubFactory(AccountFactory)
    content = factory.Faker('sentence')
    correct = factory.Faker('boolean')
    created_at = factory.Faker('date_this_decade', before_today=True)

    class Meta:
        model = CardAnswer


class CardSetFactory(factory.DjangoModelFactory):
    title = factory.Faker('sentence')
    description = factory.Faker('paragraph')
    author = factory.SubFactory(AccountFactory)
    category = factory.SubFactory(CategoryFactory)
    size = fuzzy.FuzzyChoice(list(CardSet.SizeType.attributes.keys()))
    public = factory.Faker('boolean')
    created_at = factory.Faker('date_time_between', start_date='-60d', end_date='-30d')
    updated_at = factory.Faker('date_time_between', start_date='-30d', end_date='now')

    class Meta:
        model = CardSet

    @factory.post_generation
    def questions(self, create, related_questions, **kwargs):
        if not create:
            return

        if related_questions:
            for question in related_questions:
                self.questions.add(question)
