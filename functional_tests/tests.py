from django.test import LiveServerTestCase
from selenium import webdriver

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    def tearDown(self):
        self.browser.quit()

    def test_api_front_page(self):
        # Mary has heard about an api for a pomodoro clock and wants
        # to check it out.
        
        # self.live_server_url gives a totally wrong url and the webpage looks weird.
        # self.browser.get(self.live_server_url)

        self.browser.get('http://localhost:10000')

        # She notices the page title and header mention an api root.
        self.assertIn('Api Root', self.browser.title)
