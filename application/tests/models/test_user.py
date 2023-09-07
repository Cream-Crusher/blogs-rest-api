from unittest import TestCase

from application.models import Blog, User


class UserModelTestCase(TestCase):

    def setUp(self):
        # Arrange
        self.username = f'test_user_{self._testMethodName}'
        self.password = 'test_pass'
        self.title = 'test title'
        self.description = 'test discription'

        self.user = User.objects.create(
            username=self.username,
            password=self.password
        )

    def tearDown(self):
        self.user.delete()

    def test_user_creation(self):
        """
        Проверка на создание пользователя
        """
        # act

        # assert
        self.assertEqual(self.user.username, self.username)

    def test_get_user(self):
        """
        Тест на получение данных поста
        """
        # act
        retrieved_user = User.objects.get(id=self.user.id)

        # assert
        self.assertEqual(retrieved_user, self.user)

    def test_update_user(self):
        """
        Тест на обновление данных тега
        """
        # act
        new_user = 'Updated user'

        self.user.username = new_user
        self.user.save()

        updated_user = User.objects.get(id=self.user.id)

        # assert
        self.assertEqual(updated_user.username, new_user)

    def test_str_representation(self):
        """
        Тест на вывод __str__
        """
        # act
        # assert
        self.assertEqual(str(self.user), self.username)
