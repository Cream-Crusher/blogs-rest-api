from unittest import TestCase

from application.models import Post, User
from application.views.PostViews import PostFilter


class PostFilterTest(TestCase):
    def setUp(self):
        # arrange
        self.username = f'test_user_{self._testMethodName}'
        self.password = 'testpass'
        self.title = 'test post'
        self.title_2 = 'test post 2'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.post = Post.objects.create(
            title=self.title,
            author=self.user,
        )
        self.filter_set = PostFilter({'title': self.post}, queryset=Post.objects.all())

    def tearDown(self):
        self.user.delete()
        self.post.delete()

    def test_title_filter(self):
        # act
        filtered_posts = self.filter_set.queryset

        # assert
        self.assertEqual(len(filtered_posts), 1)
        self.assertEqual(filtered_posts[0], self.post)
