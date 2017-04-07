import os
from selenium import webdriver

class NitrogenApi():
    """
    Interface to programmatically interact with Nitrogen Sports
    """

    def __init__(self):
        """
        Constructor, launch the web driver
        """

        browser_exe = '.' + os.sep + 'chromedriver' + os.sep + 'chromedriver.exe'
        self.browser = webdriver.Chrome(browser_exe)
        self.browser.implicitly_wait(15)

    def __del__(self):
        """
        Close the browser when we delete the object
        """
        
        self.browser.close()

# The following is debug/test while developing this API...
if __name__ == '__main__':
    NITRO_API = NitrogenApi()
    NITRO_API.browser.get('https://github.com')
