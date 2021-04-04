import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators.loginlocators import LoginLocators

def test_login():

    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.find_element_by_xpath(LoginLocators.TXT_USERNAME).send_keys("Admin")
    driver.find_element_by_xpath(LoginLocators.TXT_PASSWORD).send_keys("admin123")

    driver.find_element_by_xpath(LoginLocators.BTN_LOGIN).click()    