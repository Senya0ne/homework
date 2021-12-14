from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainClass:
    def __init__(self):
        pass

    _class_number = 20

    def get_local_number(self):
        return self._class_number


class BaseMethods:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_present(self, by: tuple, error_message: str, timeout: int):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by), message=error_message)

    def wait_for_elements_present(self, by: tuple, error_message: str, timeout: int):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(by), message=error_message)
        return elements

    def wait_for_element_and_click(self, by: tuple, error_message: str, timeout: int):
        element = self.wait_for_element_present(by, error_message, timeout)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, by: tuple, value: str, error_message: str, timeout: int):
        element = self.wait_for_element_present(by, error_message, timeout)
        element.send_keys(value)
        return element

    def wait_for_element_not_present(self, by: tuple, error_message: str, timeout: int):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(by), message=error_message)

    def wait_for_element_and_clear(self, by: tuple, error_message: str, timeout: int):
        element = self.wait_for_element_present(by, error_message, timeout)
        element.clear()
        return element

    def assert_element_has_text(self, by: tuple, text: str, error_message: str, timeout: int):
        element = self.wait_for_element_present(by, error_message, timeout)
        get_text = element.get_attribute("text")
        assert get_text == text, error_message
        return element

    def swipe_element_to_left(self, by: tuple, error_message: str):
        element = self.wait_for_element_present(by, error_message, timeout=5)
        left_x = element.location.get('x')
        right_x = left_x + element.size.get('width')
        upper_y = element.location.get('y')
        lower_y = upper_y + element.size.get('height')
        middle_y = (upper_y + lower_y) / 2

        TouchAction(self.driver).press(x=right_x, y=middle_y).wait(300).move_to(x=left_x, y=middle_y).release().perform()
