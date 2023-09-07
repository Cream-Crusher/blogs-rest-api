from unittest import TestCase

from application.models import Blog, User
from application.views.BlogViews import BlogFilter


class BlogFilterTestCase(TestCase):

    def setUp(self):
        # arrange
        self.username = f'test_user_{self._testMethodName}'
        self.password = 'test_pass'
        self.title = 'test title'
        self.description = 'test discription'
        self.filter_data_title = {'title': 'Test Blog 1'}
        self.filter_data_created_at = {'created_at_0': '2023-01-01', 'created_at_1': '2023-12-31'}
        self.queryset = Blog.objects.all()
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

    def test_title_filter(self):
        # act
        blog_filter = BlogFilter(data=self.filter_data_title, queryset=self.queryset)
        filtered_queryset = blog_filter.queryset

        # assert
        self.assertEqual(len(filtered_queryset), 1)

    def test_created_at_filter(self):
        # act
        blog_filter = BlogFilter(data=self.filter_data_created_at, queryset=self.queryset)
        filtered_queryset = blog_filter.queryset

        # assert
        self.assertTrue(all('2023-01-01' <= str(blog.created_at) <= '2023-12-31' for blog in filtered_queryset))
