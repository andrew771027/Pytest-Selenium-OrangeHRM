"""
@package base
WebDriver Factory class implementation
It creates a web-driver instance based on browser configurations
"""
# -*- coding: utf-8 -*

import os

from .chrome import ChromeDriver
from .firefox import FirefoxDriver

class WebDriverFactory:

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        :Returns None:
        """
        self.browser = browser

    def get_WebDriver_Instance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return 'WebDriver Instance':
        """

        if self.browser in ["firefox", "ff"]:
            webdriver = FirefoxDriver()
            self.driver = webdriver.get_firefoxdriver()

        elif self.browser in ["headlessfirefox"]:
            webdriver = FirefoxDriver()
            self.driver = webdriver.get_headless_firefoxdriver()

        elif self.browser in ["chrome", "gc", "googlechrome"]:
            webdriver = ChromeDriver()
            self.driver = webdriver.get_chromedriver()    

        elif self.browser in ["headlesschrome"]: 
            webdriver = ChromeDriver()
            self.driver = webdriver.get_headless_chromedriver()    

        else:
            webdriver = ChromeDriver()
            self.driver = webdriver.get_chromedriver()    


        self.driver.set_window_size(1440, 900)
        self.driver.delete_all_cookies()

        return self.driver