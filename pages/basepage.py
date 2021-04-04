import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGGER = logging.getLogger(__name__)

class BasePage:

    def __init__(self, driver):
        self.driver=driver
        self.explicty_wait=20
        self.implicity_wait=10
        self.timeout=60

    def open_page(self, url):

        self.driver.get(url)
    
    def get_titile(self) -> str:
        
        return self.driver.title
    
    def get_elements(self, locator) -> list:

        try:

            elements = WebDriverWait(self.driver, self.explicty_wait).until(
                EC.presence_of_element_located(locator=locator)
            )

            return elements
        
        except Exception as e:
            LOGGER.error(f"Element {locator} can not get.")
            LOGGER.error(f"Reason: {e}.")
            raise e
        
    def click_element(self, locator) -> None:

        try:

            element = self.get_elements(locator=locator)
            element.click()
            
        except Exception as e:
            LOGGER.error(f"Can not click element {locator}.")
            LOGGER.error(f"Reason: {e}")
            raise e
    
    def input_text(self, locator, text) -> None:

        self.delete_text(locator=locator)
        element = self.get_elements(locator=locator)
        element.send_keys(text)
        
    def delete_text(self, locator) -> None:

        element = self.get_elements(locator=locator)
        element.clear()
    
