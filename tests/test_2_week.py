from src.MainClass import BaseMethods
from selenium.webdriver.common.by import By


def test_search_element_has_text(driver):
    driver = BaseMethods(driver)
    driver.assert_element_has_text((By.XPATH, "//*[contains(@text,'Search Wikipedia')]"), "Search Wikipedia",
                                   "Not found text 'Search Wikipedia' ", 5)
