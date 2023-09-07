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

    def test_get_tag(self):
        """
        Тест на получение данных поста
        """
        # act
        retrieved_tag = Tag.objects.get(id=self.tag.id)

        # assert
        self.assertEqual(retrieved_tag, self.tag)

    def test_update_tag(self):
        """
        Тест на обновление данных тега
        """
        # act
        new_tag_name = 'Updated Title'

        self.tag.tag_name = new_tag_name
        self.tag.save()

        updated_tag = Tag.objects.get(id=self.tag.id)

        # assert
        self.assertEqual(updated_tag.tag_name, new_tag_name)

    def test_str_representation(self):
        """
        Тест на вывод __str__
        """
        # act
        # assert
        self.assertEqual(str(self.tag_name), self.tag_name)
