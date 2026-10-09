import unittest
from crawl import normalize_url, get_heading_from_html, get_first_paragraph_from_html, get_urls_from_html



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

if __name__ == "__main__":
    unittest.main()
