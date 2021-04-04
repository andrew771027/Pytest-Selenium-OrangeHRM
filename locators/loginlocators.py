from selenium.webdriver.common.by import By
class LoginLocators:

    TXT_USERNAME = (By.XPATH, ".//input[@id='txtUsername']")
    TXT_PASSWORD = (By.XPATH, ".//input[@id='txtPassword']")

    BTN_LOGIN = (By.XPATH, ".//input[@id='btnLogin']")
    BTN_FORGOTPASSWORD = (By.XPATH, ".//div[@id='forgotPasswordLink']/a")