from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainClass:
    def __init__(self):
        pass

    _class_number = 20

    def get_local_number(self):
        return self._class_number


class MainPageObject:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_present(self, locator: str, error_message: str, timeout: int):
        by = self.get_locator_by_string(locator)
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by), message=error_message)

    def wait_for_elements_present(self, locator: str, error_message: str, timeout: int):
        by = self.get_locator_by_string(locator)
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(by),
                                                         message=error_message)

    def wait_for_element_and_click(self, locator: str, error_message: str, timeout: int):
        element = self.wait_for_element_present(locator, error_message, timeout)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, locator, value: str, error_message: str, timeout: int):
        element = self.wait_for_element_present(locator, error_message, timeout)
        element.send_keys(value)
        return element

    def wait_for_element_not_present(self, locator: str, error_message: str, timeout: int):
        by = self.get_locator_by_string(locator)
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(by), message=error_message)

    def wait_for_element_and_clear(self, locator: str, error_message: str, timeout: int):
        element = self.wait_for_element_present(locator, error_message, timeout)
        element.clear()
        return element

    def assert_element_has_text(self, locator: str, text: str, error_message: str, timeout: int):
        element = self.wait_for_element_present(locator, error_message, timeout)
        get_text = element.get_attribute("text")
        assert get_text == text, error_message
        return element

    def swipe_element_to_left(self, locator: str, error_message: str):
        element = self.wait_for_element_present(locator, error_message, timeout=5)
        left_x = element.location.get('x')
        right_x = left_x + element.size.get('width')
        upper_y = element.location.get('y')
        lower_y = upper_y + element.size.get('height')
        middle_y = (upper_y + lower_y) / 2

        TouchAction(self.driver).press(x=right_x, y=middle_y).wait(300).move_to(x=left_x,
                                                                                y=middle_y).release().perform()

    def get_locator_by_string(self, locator_with_type: str):
        exploded_locator = locator_with_type.split(":", 1)
        by_type = exploded_locator[0]
        locator = exploded_locator[1]
        if by_type == 'xpath':
            return By.XPATH, locator
        elif by_type == 'id':
            return By.ID, locator
        else:
            raise ValueError("Cannot get type of locator. locator" + locator_with_type)
