import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        else:
            self.live_server_url = 'http://localhost:10000'

    def tearDown(self):
        self.browser.quit()

    def test_api_front_page(self):
        # Mary has heard about an api for a pomodoro clock and wants
        # to check it out.

        # self.live_server_url gives a totally wrong url and the webpage looks weird.
        # self.browser.get(self.live_server_url)

        self.browser.get(self.live_server_url)

        # She notices the page title and header mention an api root.
        self.assertIn('Api Root', self.browser.title)
