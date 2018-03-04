from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    def tearDown(self):
        self.browser.quit()

    def test_api_front_page(self):
        # Mary has heard about an api for a pomodoro clock and wants
        # to check it out.
        self.browser.get('http://localhost:10000')

        # She notices the page title and header mention an api root.
        self.assertIn('Api Root', self.browser.title)


if __name__ == '__main__':
    unittest.main()
