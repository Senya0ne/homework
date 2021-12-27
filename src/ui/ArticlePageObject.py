from selenium.webdriver.common.by import By

from .MainPageObject import MainPageObject


class ArticlePageObject(MainPageObject):
    ARTICLE_TITLE = "id:org.wikipedia:id/view_page_title_text"
    LIST_ARTICLES = "id:org.wikipedia:id/page_list_item_container"
    FOOTER_ELEMENT = "xpath://*[@text='View page in browser']"
    OPTIONS_BUTTON = "xpath://android.widget.ImageView[@content-desc='More options']"
    OPTIONS_ADD_TO_MY_LIST_BUTTON = "xpath://*[@text='Add to reading list']"
    ADD_TO_MY_LIST_OVERLAY = "id:org.wikipedia:id/onboarding_button"
    MY_LIST_NAME_INPUT = "id:org.wikipedia:id/text_input"
    MY_LIST_OK_BUTTON = "xpath://*[@text='OK']"
    CLOSE_ARTICLE_BUTTON = "xpath://android.widget.ImageButton[@content-desc='Navigate up']"
    NAME_OF_FOLDER = "Learning Programming"
    READING_LIST = "id:org.wikipedia:id/snackbar_action"
    DIRECTORY_WITH_ARTICLES = f"xpath://*[@resource-id='org.wikipedia:id/item_container']//*[@text='{NAME_OF_FOLDER}']"

    def wait_for_title_element(self):
        return self.wait_for_element_present(self.ARTICLE_TITLE, "Cannot find title for article", 20)

    def get_article_title(self):
        title_element = self.wait_for_title_element()
        return title_element.get_attribute("text")

    def get_list_articles(self):
        elements = self.wait_for_elements_present(self.LIST_ARTICLES, "Not found elements in search results",
                                                  15)
        return elements

    def add_article_to_my_list(self):
        self.wait_for_element_and_click(
            self.OPTIONS_BUTTON,
            "Cannot find button to open article options",
            15)
        self.wait_for_element_and_click(self.OPTIONS_ADD_TO_MY_LIST_BUTTON,
                                        "Cannot find option to add article to reading list",
                                        15)
        self.wait_for_element_and_click(self.ADD_TO_MY_LIST_OVERLAY,
                                        "Cannot find 'GOT IT' tip overlay",
                                        15)
        self.wait_for_element_and_clear(self.MY_LIST_NAME_INPUT,
                                        "Cannot find input to set name of articles folder",
                                        15)
        self.wait_for_element_and_send_keys(self.MY_LIST_NAME_INPUT,
                                            self.NAME_OF_FOLDER,
                                            "Cannot put text into articles folder input",
                                            5)
        self.wait_for_element_and_click(self.MY_LIST_OK_BUTTON,
                                        "Cannot press OK button",
                                        5)

    def add_second_article_to_my_list(self):
        self.wait_for_element_and_click(self.OPTIONS_BUTTON,
                                        "Cannot find button to open article options",
                                        15)
        self.wait_for_element_and_click(self.OPTIONS_ADD_TO_MY_LIST_BUTTON,
                                        "Cannot find option to add article to reading list",
                                        15)
        self.wait_for_element_and_click(self.DIRECTORY_WITH_ARTICLES,
                                        "Cannot find option to add article to reading list",
                                        15)
        self.wait_for_element_and_click(self.READING_LIST,
                                        "Cannot find element for redirect to reading list",
                                        6)

    def close_article(self):
        return self.wait_for_element_and_click(self.CLOSE_ARTICLE_BUTTON,
                                               "Cannot close article, cannot find x link",
                                               5)
