from src.MainClass import BaseMethods
from selenium.webdriver.common.by import By


def test_search_element_has_text(driver):
    driver = BaseMethods(driver)
    driver.assert_element_has_text((By.XPATH, "//*[contains(@text,'Search Wikipedia')]"), "Search Wikipedia",
                                   "Not found text 'Search Wikipedia' ", 5)


def test_search_articles_and_cancel_search(driver):
    driver = BaseMethods(driver)
    driver.wait_for_element_and_click((By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
                                      "Not found element Search Wikipedia", 5)
    driver.wait_for_element_and_send_keys((By.ID, "org.wikipedia:id/search_src_text"),
                                          "Python", "Not found input for search", 10)
    list_elements = driver.wait_for_elements_present(
        (By.ID, "org.wikipedia:id/page_list_item_container"),
        "Not found elements in search results", 10)
    assert len(list_elements) > 1
    driver.wait_for_element_and_clear((By.ID, "org.wikipedia:id/search_src_text"),
                                      "Cannot find search field",
                                      5)
    driver.wait_for_element_and_click((By.ID, "org.wikipedia:id/search_close_btn"),
                                      "Not found x button to cancel search",
                                      5)
    driver.wait_for_element_not_present((By.ID, "org.wikipedia:id/search_close_btn"),
                                        "X is still present on the page", 5)

