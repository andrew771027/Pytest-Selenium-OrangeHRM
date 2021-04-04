import pytest
from selenium import webdriver

from pages.loginpage import LoginPage

def test_login():

    driver = webdriver.Chrome()
    # driver.get("https://opensource-demo.orangehrmlive.com/")   

    login_page = LoginPage(driver)
    login_page.open_page(url="https://opensource-demo.orangehrmlive.com/")
    login_page.input_username(username="Admin")
    login_page.input_password(password="admin123")
    login_page.click_login_btn()