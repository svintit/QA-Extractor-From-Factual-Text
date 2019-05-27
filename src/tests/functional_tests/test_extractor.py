import os
import time
import unittest

from selenium import webdriver


class Test_Extractor(unittest.TestCase):

    def setUp(self):
        caps = {
            'browserName': os.getenv('BROWSER', 'chrome')
        }
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_extractor_homepage(self):
        browser = self.browser
        browser.get('https://extractor.thesvinti.com/')

        time.sleep(1)
        self.assertIn('Extract Questions', browser.page_source)

    def test_extractor_go_to_login(self):
        browser = self.browser
        browser.get('https://extractor.thesvinti.com/')

        btn = browser.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[6]/a')
        btn.click()

        time.sleep(1)
        self.assertIn('Login', browser.page_source)

    def test_extractor_go_to_register(self):
        browser = self.browser
        browser.get('https://extractor.thesvinti.com/')

        btn = browser.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[7]/a')
        btn.click()

        time.sleep(1)
        self.assertIn('Sign Up!', browser.page_source)

    def test_extractor_add_text(self):
        btnclicked = False
        browser = self.browser
        browser.get('https://extractor.thesvinti.com/')

        btn = browser.find_element_by_xpath('//*[@id="myBtn"]')
        try:
            btn.click()
        finally:
            btnclicked = True

        time.sleep(1)
        self.assertTrue(btnclicked)

    def test_extractor_login_user(self):
        browser = self.browser
        browser.get('https://extractor.thesvinti.com/login')

        email_input = browser.find_element_by_xpath('//*[@id="email"]')
        email_input.clear()
        email_input.send_keys('admin@thesvinti.com')

        pass_input = browser.find_element_by_xpath('//*[@id="password"]')
        pass_input.clear()
        pass_input.send_keys('admin')

        btn = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/button')
        btn.click()

        time.sleep(1)
        self.assertEqual('https://extractor.thesvinti.com/', browser.current_url)

    def test_extractor_output_questions_as_user(self):
        browser = self.browser
        browser.get('https://extractor.thesvinti.com/login')

        email_input = browser.find_element_by_xpath('//*[@id="email"]')
        email_input.clear()
        email_input.send_keys('admin@thesvinti.com')

        pass_input = browser.find_element_by_xpath('//*[@id="password"]')
        pass_input.clear()
        pass_input.send_keys('admin')

        btn = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/button')
        btn.click()

        btn = browser.find_element_by_xpath('//*[@id="myBtn"]')
        btn.click()

        text_input = browser.find_element_by_xpath('//*[@id="post-text"]')

        time.sleep(1)
        self.assertIn('Inputted Text', browser.page_source)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
