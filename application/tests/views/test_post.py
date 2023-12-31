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
        self.filter_data_created_at = {'created_at_0': '2023-01-01', 'created_at_1': '2023-12-31'}
        self.queryset = Post.objects.all()

    def tearDown(self):
        self.user.delete()
        self.post.delete()

    def test_title_filter(self):
        # act
        self.filter_set = PostFilter({'title': self.post}, queryset=self.queryset)
        filtered_posts = self.filter_set.queryset

        # assert
        self.assertEqual(len(filtered_posts), 1)
        self.assertEqual(filtered_posts[0], self.post)

    def test_created_at_filter(self):
        # act
        blog_filter = PostFilter(data=self.filter_data_created_at, queryset=self.queryset)
        filtered_queryset = blog_filter.queryset

        # assert
        self.assertTrue(all('2023-01-01' <= str(blog.created_at) <= '2023-12-31' for blog in filtered_queryset))
