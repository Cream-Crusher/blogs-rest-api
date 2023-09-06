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
        self.blog = Blog.objects.create(
            title=self.title,
            description=self.description,
            owner=self.user
        )

    def tearDown(self):
        self.user.delete()
        self.blog.delete()

    def test_user_creation(self):
        """
        Проверка на создание пользователя
        """
        # act

        # assert
        self.assertEqual(self.user.username, self.username)

    def test_str_representation(self):
        """
        Тест на вывод __str__
        """
        # act
        # assert
        self.assertEqual(str(self.user), self.username)
