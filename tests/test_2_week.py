from src.ui.ArticlePageObject import ArticlePageObject
from src.ui.MainPageObject import MainPageObject
from selenium.webdriver.common.by import By

from src.ui.SearchPageObject import SearchPageObject


def test_search_element_has_text(driver):
    driver = MainPageObject(driver)
    driver.assert_element_has_text((By.XPATH, "//*[contains(@text,'Search Wikipedia')]"), "Search Wikipedia",
                                   "Not found text 'Search Wikipedia' ", 5)


def test_search_articles_and_cancel_search(driver):
    search_page_object = SearchPageObject(driver)
    search_page_object.init_search_input()
    search_page_object.type_search_line("Python")

    article_page_object = ArticlePageObject(driver)
    list_elements = article_page_object.get_list_articles()
    assert len(list_elements) > 1

    search_page_object.clear_search_input()
    search_page_object.cancel_search()
    search_page_object.wait_for_cancel_button_to_disappear()

