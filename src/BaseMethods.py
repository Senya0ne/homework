from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethods:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_present(self, by: tuple, error_message: str, timeout: int):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by), message=error_message)

    def wait_for_elements_present(self, by: tuple, error_message: str, timeout: int):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(by),
                                                             message=error_message)
        return elements

    def rotate_landscape(self):
        return self.driver.orientation('LANDSCAPE')

    def rotate_portrait(self):
        return self.driver.orientation('PORTRAIT')
