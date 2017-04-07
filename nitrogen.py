from bs4 import BeautifulSoup
import os
from selenium import webdriver
from time import sleep

class NitrogenApi():
    """
    Interface to programmatically interact with Nitrogen Sports
    """

    def __init__(self):
        """
        Constructor, launch the web driver
        """

        self.browser = None
        # Get this person's Nitrogen login credentials from env vars
        self.login_user = os.getenv('NitrogenUser')
        if self.login_user is None:
            print('You must set environment variable "NitrogenUser" to your username')
            exit()
        self.login_pass = os.getenv('NitrogenPass')
        if self.login_pass is None:
            print('You must set environment variable "NitrogenPass" to your password')
            exit()
        # Set up the browser driver
        browser_exe = '.' + os.sep + 'chromedriver' + os.sep + 'chromedriver.exe'
        self.browser = webdriver.Chrome(browser_exe)
        self.browser.implicitly_wait(5)

    def login(self):
        """
        Log in to Nitrogen Sports
        """
        self.browser.get('https://nitrogensports.eu')
        sleep(15)
        self.browser.find_element_by_css_selector('div#modal-welcome-login-button').click()
        sleep(5)
        self.browser.find_element_by_css_selector('#modal-account-login-username-textbox').send_keys(self.login_user)
        self.browser.find_element_by_css_selector('#modal-account-login-password-textbox').send_keys(self.login_pass)
        self.browser.find_element_by_css_selector('#modal-account-login-button').click()

'''    def __del__(self):
        """
        Close the browser when we delete the object
        """

        if self.browser is not None:
            self.browser.close()'''

# The following is debug/test while developing this API...
if __name__ == '__main__':
    NITRO_API = NitrogenApi()
    NITRO_API.login()
