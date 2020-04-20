import factory
from users.models import User

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username_{0}'.format(n))
    password = 'test'
    nick = factory.Faker('first_name')