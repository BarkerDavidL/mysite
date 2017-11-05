from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_view_blog(self):

        # Dave wants to view a blog site
        self.browser.get('http://localhost:8000')

        # He sees the blog page and a header about Blogs
        assert 'Blog' in self.browser.title
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Blog', header_text)


if __name__ in '__main__':
    unittest.main()

