from .basepage import BasePage
from locators.loginlocators import LoginLocators

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        
    def input_username(self, username : str) -> None:
        self.input_text(locator=LoginLocators.TXT_USERNAME, text=username)

    def input_password(self, password : str) -> None:
        self.input_text(locator=LoginLocators.TXT_PASSWORD, text=password)

    def click_login_btn(self):
        self.click_element(locator=LoginLocators.BTN_LOGIN)
