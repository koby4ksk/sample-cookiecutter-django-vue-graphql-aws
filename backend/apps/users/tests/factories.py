import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    username = 'user'
    email = 'test-name@example.com'
    full_name = 'test name'
