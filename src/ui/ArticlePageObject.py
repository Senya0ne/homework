from selenium.webdriver.common.by import By

from .MainPageObject import MainPageObject


class ArticlePageObject(MainPageObject):
    ARTICLE_TITLE = "org.wikipedia:id/view_page_title_text"
    LIST_ARTICLES = "org.wikipedia:id/page_list_item_container"
    FOOTER_ELEMENT = "//*[@text='View page in browser']"
    OPTIONS_BUTTON = "//android.widget.ImageView[@content-desc='More options']"
    OPTIONS_ADD_TO_MY_LIST_BUTTON = "//*[@text='Add to reading list']"
    ADD_TO_MY_LIST_OVERLAY = "org.wikipedia:id/onboarding_button"
    MY_LIST_NAME_INPUT = "org.wikipedia:id/text_input"
    MY_LIST_OK_BUTTON = "//*[@text='OK']"
    CLOSE_ARTICLE_BUTTON = "//android.widget.ImageButton[@content-desc='Navigate up']"
    NAME_OF_FOLDER = "Learning Programming"
    READING_LIST = "org.wikipedia:id/snackbar_action"

    def wait_for_title_element(self):
        return self.wait_for_element_present((By.ID, self.ARTICLE_TITLE), "Cannot find title for article", 20)

    def get_article_title(self):
        title_element = self.wait_for_title_element()
        return title_element.get_attribute("text")

    def get_list_articles(self):
        elements = self.wait_for_elements_present((By.ID, self.LIST_ARTICLES), "Not found elements in search results",
                                                  15)
        return elements

    def add_article_to_my_list(self):
        self.wait_for_element_and_click((By.XPATH,
                                         self.OPTIONS_BUTTON),
                                        "Cannot find button to open article options",
                                        15)
        self.wait_for_element_and_click((By.XPATH,
                                         self.OPTIONS_ADD_TO_MY_LIST_BUTTON),
                                        "Cannot find option to add article to reading list",
                                        15)
        self.wait_for_element_and_click((By.ID,
                                         self.ADD_TO_MY_LIST_OVERLAY),
                                        "Cannot find 'GOT IT' tip overlay",
                                        15)
        self.wait_for_element_and_clear((By.ID,
                                         self.MY_LIST_NAME_INPUT),
                                        "Cannot find input to set name of articles folder",
                                        15)
        self.wait_for_element_and_send_keys((By.ID, self.MY_LIST_NAME_INPUT),
                                            self.NAME_OF_FOLDER,
                                            "Cannot put text into articles folder input",
                                            5)
        self.wait_for_element_and_click((By.XPATH, self.MY_LIST_OK_BUTTON),
                                        "Cannot press OK button",
                                        5)

    def add_second_article_to_my_list(self):
        self.wait_for_element_and_click((By.XPATH,
                                         self.OPTIONS_BUTTON),
                                        "Cannot find button to open article options",
                                        15)
        self.wait_for_element_and_click((By.XPATH,
                                         self.OPTIONS_ADD_TO_MY_LIST_BUTTON),
                                        "Cannot find option to add article to reading list",
                                        15)
        self.wait_for_element_and_click((By.XPATH,
                                         f"//*[@resource-id='org.wikipedia:id/item_container']//*[@text='{self.NAME_OF_FOLDER}']"),
                                        "Cannot find option to add article to reading list",
                                        15)
        self.wait_for_element_and_click((By.ID, self.READING_LIST),
                                        "Cannot find element for redirect to reading list",
                                        6)

    def close_article(self):
        return self.wait_for_element_and_click((By.XPATH, self.CLOSE_ARTICLE_BUTTON),
                                               "Cannot close article, cannot find x link",
                                               5)
