import unittest
from crawl import normalize_url, get_heading_from_html, get_first_paragraph_from_html, get_urls_from_html, get_images_from_html, extract_page_data



class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_1(self):
        input_url = "https://www.boot.dev/blog/path/"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_2(self):
        input_url = "http://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_3(self):
        input_url = "http://www.boot.dev/blog/path/"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_0(self):
        html = '''<html>
          <body>
            <h1>Welcome to Boot.dev</h1>
            <main>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
          </body>
        </html>'''
        actual = get_heading_from_html(html)
        expected = 'Welcome to Boot.dev'
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_1(self):
        html = '''<html>
          <body>
            <main>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
            <h2>This is a new heading</h2>
          </body>
        </html>'''
        actual = get_heading_from_html(html)
        expected = 'This is a new heading'
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_2(self):
        html = '''<html>
          <body>
            <main>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph.</p>
            </main>
          </body>
        </html>'''
        actual = get_heading_from_html(html)
        expected = ''
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html(self):
        html = '''
        <html>
          <body>
            <h1>Welcome to boot.dev</h1>
            <main>
              <p>Learn to code by building real projects.</p>
              <p>This is the second paragraph</p>
            </main>
          </body>
        </html>
        '''
        actual = get_first_paragraph_from_html(html)
        expected = 'Learn to code by building real projects.'
        self.assertEqual(actual, expected)


    def test_get_first_paragraph_from_html_1(self):
        html = '''
        <html>
          <body>
            <h1>Welcome to boot.dev</h1>
          </body>
        </html>
        '''
        actual = get_first_paragraph_from_html(html)
        expected = ''
        self.assertEqual(actual, expected)


    def test_get_first_paragraph_from_html_2(self):
        html = '''
        <html>
          <body>
            <h1>Welcome to boot.dev</h1>
            <p>Learn to code by building real projects.</p>
            <p>This is the second paragraph</p>
          </body>
        </html>
        '''
        actual = get_first_paragraph_from_html(html)
        expected = 'Learn to code by building real projects.'
        self.assertEqual(actual, expected)

    def test_get_urls_from_html(self):
        input_url = 'https://crawler-test.com'
        input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ['https://crawler-test.com']
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_1(self):
        input_url = 'https://crawler-test.com'
        input_body = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a><a href="https://www.google.com"</a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ['https://crawler-test.com', 'https://www.google.com']
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_2(self):
        input_url = 'https://crawler-test.com'
        input_body = '<html><body><p>Some Text.</p><a>anchor</a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

    def test_get_images_from_html(self):
        input_url = 'https://crawler-test.com'
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ['https://crawler-test.com/logo.png']
        self.assertEqual(actual, expected)

    def test_get_images_from_html_1(self):
        input_url = 'https://crawler-test.com'
        input_body = '<html><body><img src="/logo.png" alt="Logo"><img src="/dog.png" alt="Dog"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ['https://crawler-test.com/logo.png', 'https://crawler-test.com/dog.png']
        self.assertEqual(actual, expected)

    def test_get_images_from_html_2(self):
        input_url = 'https://crawler-test.com'
        input_body = '<html><body><img alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

    def test_extract_page_data(self):
        input_url = 'https://crawler-test.com'
        input_body = '''<html><body>
            <h1>Test Title</h1>
            <p>This is the first paragraph.</p>
            <a href="/link1"Link 1</a>
            <img src="/image1.jpg" alt="Image 1">
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
            'url': 'https://crawler-test.com',
            'heading': 'Test Title',
            'first_paragraph': 'This is the first paragraph.',
            'outgoing_links': ['https://crawler-test.com/link1'],
            'image_urls': ['https://crawler-test.com/image1.jpg'],
        }
        self.assertEqual(actual, expected)

    def test_extract_page_data_1(self):
        input_url = 'https://crawler-test.com'
        input_body = '''<html><body>
            <h1>Test Title</h1>
            <p>This is the first paragraph.</p>
            <a href="/link1"Link 1</a>
            <img src="/image1.jpg" alt="Image 1">
            <h1>Second Test Title]</h1>
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
            'url': 'https://crawler-test.com',
            'heading': 'Test Title',
            'first_paragraph': 'This is the first paragraph.',
            'outgoing_links': ['https://crawler-test.com/link1'],
            'image_urls': ['https://crawler-test.com/image1.jpg'],
        }
        self.assertEqual(actual, expected)

    def test_extract_page_data_2(self):
        input_url = 'https://crawler-test.com'
        input_body = '''<html><body>
            <h1>Test Title</h1>
            <p>This is the first paragraph.</p>
            <a href="/link1"Link 1</a>
            <p>This is the second paragraph</p>
            <img src="/image1.jpg" alt="Image 1">
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
            'url': 'https://crawler-test.com',
            'heading': 'Test Title',
            'first_paragraph': 'This is the first paragraph.',
            'outgoing_links': ['https://crawler-test.com/link1'],
            'image_urls': ['https://crawler-test.com/image1.jpg'],
        }
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
