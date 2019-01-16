import factory

from django.contrib.auth import get_user_model
from django.utils import timezone

from account.models import Account


User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('safe_email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = User


class AccountFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    created_at = factory.Faker('date_time_between', start_date='-60d', end_date='-30d', tzinfo=timezone.utc)
    updated_at = factory.Faker('date_time_between', start_date='-30d', end_date='now', tzinfo=timezone.utc)

    class Meta:
        model = Account
