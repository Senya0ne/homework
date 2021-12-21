from selenium.webdriver.common.by import By

from .MainPageObject import MainPageObject


class SearchPageObject(MainPageObject):
    SUBSTRING = None
    SEARCH_INIT_ELEMENT = "//*[contains(@text,'Search Wikipedia')]"
    SEARCH_INPUT = "//*[contains(@text, 'Search…')]"
    SEARCH_CANCEL_BUTTON = "org.wikipedia:id/search_close_btn"
    SEARCH_RESULT_BY_SUBSTRING_TPL = f"//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='{SUBSTRING}']"
    SEARCH_RESULT_ELEMENT = "//*[@resource-id='org.wikipedia:id/search_results_list']/*[@resource-id='org.wikipedia:id/page_list_item_container']"
    SEARCH_EMPTY_RESULT_LABEL = "//*[@text='No results found']"
    INPUT_AFTER_SEARCH = "org.wikipedia:id/search_src_text"

    def get_result_search_element(self, substring: str):
        """Template method for help get name search element"""
        return self.SEARCH_RESULT_BY_SUBSTRING_TPL.replace(f"{self.SUBSTRING}", substring)

    def init_search_input(self):
        self.wait_for_element_and_click((By.XPATH, self.SEARCH_INIT_ELEMENT),
                                        "Cannot find search Wikipedia input", 5)

    def type_search_line(self, search_string: str):
        self.wait_for_element_and_send_keys((By.XPATH, self.SEARCH_INPUT), search_string,
                                            "Cannot find search input", 5)

    def click_by_article_with_substring(self, substring: str):
        search_result_xpath = self.get_result_search_element(substring)
        self.wait_for_element_and_click((By.XPATH, search_result_xpath),
                                        "Cannot find and click search result with substring" + substring, 10)

    def clear_search_input(self):
        self.wait_for_element_and_clear((By.ID, self.INPUT_AFTER_SEARCH),
                                        "Cannot find search field",
                                        5)

    def cancel_search(self):
        self.wait_for_element_and_click((By.ID, self.SEARCH_CANCEL_BUTTON),
                                        "Not found x button to cancel search",
                                        5)

    def wait_for_cancel_button_to_disappear(self):
        self.wait_for_element_not_present((By.ID, self.SEARCH_CANCEL_BUTTON),
                                          "X is still present on the page", 5)
