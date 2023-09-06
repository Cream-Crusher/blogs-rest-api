from unittest import TestCase

from application.models import Tag


class TagModelTestCase(TestCase):

    def setUp(self):
        # Arrange
        self.tag_name = 'tag_name'

        self.tag = Tag.objects.create(
            tag_name=self.tag_name
        )

    def tearDown(self):
        self.tag.delete()

    def test_blog_creation(self):
        """
        Проверка на create
        """
        # act
        # assert
        self.assertEqual(self.tag.tag_name, self.tag_name)

    def test_str_representation(self):
        """
        Тест на вывод __str__
        """
        # act
        # assert
        self.assertEqual(str(self.tag_name), self.tag_name)
