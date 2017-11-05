from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from blog.views import home_page
from blog.models import Post

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returms_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Blog</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

class PostModelTest(TestCase):

    def test_saving_and_retrieving_posts(self):
        first_post = Post()
        first_post.title = 'The first post'
        first_post.text = 'first blog text'
        first_post.save()

        second_post = Post()
        second_post.title = 'The second post'
        second_post.text = 'second blog text'
        second_post.save()

        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 2)

        first_saved_post = saved_posts[0]
        second_saved_post = saved_posts[1]
        self.assertEqual(first_saved_post.title, 'The first post')
        self.assertEqual(first_saved_post.text, 'first blog text')
        self.assertEqual(second_saved_post.title, 'The second post')
        self.assertEqual(second_saved_post.text, 'second blog text')

