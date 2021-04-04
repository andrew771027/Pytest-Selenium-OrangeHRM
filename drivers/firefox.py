# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class FirefoxDriver():

    def __init__(self):
        
        self.options = Options()
        self.options.add_argument("--lang=en-us")
        self.options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
        self.options.add_argument("--incognito")
        
    def get_firefoxdriver(self) -> webdriver:
        
        return webdriver.Firefox(options=self.options)
    
    def get_headless_firefoxdriver(self) -> webdriver:
        
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")

        return webdriver.Firefox(options=self.options)

