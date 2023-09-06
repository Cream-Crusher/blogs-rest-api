from unittest import TestCase

from application.models import Blog, User, Post


class BlogModelTestCase(TestCase):

    def setUp(self):
        # Arrange
        self.username = 'test_user'
        self.password = 'test_pass'
        self.title = 'test title'
        self.description = 'test discription'
        self.content = 'test content'

        self.user = User.objects.create(
            username=self.username,
            password=self.password
        )
        self.blog = Blog.objects.create(
            title=self.title,
            description=self.description,
            owner=self.user
        )
        self.post = Post.objects.create(
            title=self.title,
            body=self.content,
            author=self.user
        )

    def tearDown(self):
        self.user.delete()
        self.blog.delete()
        self.post.delete()

    def test_blog_creation(self):
        """
        Проверка на create
        """
        # act
        # assert
        self.assertEqual(self.blog.title, self.title)
        self.assertEqual(self.blog.description, self.description)
        self.assertEqual(self.blog.owner, self.user)
        self.assertIsNotNone(self.blog.created_at)
        self.assertIsNotNone(self.blog.updated_at)

    def test_str_representation(self):
        """
        Тест на вывод __str__
        """
        # act
        # assert
        self.assertEqual(str(self.blog), self.title)

    def test_updated_at(self):
        """
        Тест на правильное обновление времени
        """
        # act
        initial_updated_at = self.blog.updated_at

        self.blog.description = 'now'
        self.blog.save()

        # assert
        self.assertNotEqual(initial_updated_at, self.blog.updated_at)

    def test_created_at(self):
        """
        Тест на правильное создание времени
        """
        # act
        initial_create_at = self.blog.created_at

        self.blog.description = 'now'

        # assert
        self.assertEqual(initial_create_at, self.blog.created_at)

    def test_add_author(self):
        """
        Тест на добавление авторов
        """
        # act
        self.blog.authors.add(self.user)

        authors_blog = [user.id for user in self.blog.authors.all()]

        # assert
        self.assertIn(self.user.id, authors_blog)

    def test_add_post(self):
        """
        Тест на добавление поста
        """
        # act
        self.blog.posts.add(self.post)

        posts_blog = [user.id for user in self.blog.posts.all()]

        # assert
        self.assertIn(self.post.id, posts_blog)
