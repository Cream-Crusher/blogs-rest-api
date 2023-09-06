from unittest import TestCase

from application.models import Tag, User, Post


class BlogModelTestCase(TestCase):

    def setUp(self):
        # Arrange
        self.username = 'test_user'
        self.password = 'test_pass'
        self.title = 'test title'
        self.body = 'test body'
        self.tag_title = 'tag_name'

        self.user = User.objects.create(
            username=self.username,
            password=self.password
        )
        self.tag = Tag.objects.create(
            tag_name=self.tag_title
        )
        self.post = Post.objects.create(
            author=self.user,
            title=self.title,
            body=self.body
        )

    def tearDown(self):
        self.user.delete()
        self.tag.delete()
        self.post.delete()

    def test_blog_creation(self):
        """
        Проверка на create
        """
        # act
        # assert
        self.assertEqual(self.post.title, self.title)
        self.assertEqual(self.post.body, self.body)
        self.assertIsNotNone(self.post.created_at)
        self.assertIsNotNone(self.post.is_published)

    def test_str_representation(self):
        """
        Тест на вывод __str__
        """
        # act
        # assert
        self.assertEqual(str(self.post), self.title)

    def test_created_at(self):
        """
        Тест на правильное создание времени
        """
        # act
        initial_create_at = self.post.created_at

        self.post.description = 'now'

        # assert
        self.assertEqual(initial_create_at, self.post.created_at)

    def test_add_tag(self):
        """
        Тест на добавление тегов
        """
        # act
        self.post.tags.add(self.tag)

        tags_post = [tag.id for tag in self.post.tags.all()]

        # assert
        self.assertIn(self.tag.id, tags_post)

    def test_add_like(self):
        """
        Тест на добавление лайков
        """
        # act
        self.post.likes.add(self.user)

        likes_post = [user.id for user in self.post.likes.all()]

        # assert
        self.assertIn(self.user.id, likes_post)

    def test_loading_db_queries(self):
        # Act
        posts = Post.objects.loading_db_queries()

        # Assert
        self.assertTrue(posts._prefetch_related_lookups)

    def test_count_like(self):
        # Act
        posts = Post.objects.count_like()

        # Assert
        self.assertTrue(posts.query.annotations.get('like_count'))
