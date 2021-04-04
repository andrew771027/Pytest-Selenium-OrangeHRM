# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ChromeDriver():

    def __init__(self):
        
        self.options = Options()
        self.options.add_argument("--lang=en-us")
        self.options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
        self.options.add_argument("--incognito")
        
    def get_chromedriver(self) -> webdriver:
        
        return webdriver.Chrome(options=self.options)
    
    def get_headless_chromedriver(self) -> webdriver:
        
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")

        return webdriver.Chrome(options=self.options)
