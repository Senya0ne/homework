from selenium.webdriver.common.by import By

from .MainPageObject import MainPageObject


class MyListsPageObject(MainPageObject):
    FOLDER_NAME = None
    TITLE = None
    DESCRIPTION = None
    LANGUAGE = None
    FOLDER_BY_NAME_TPL = f"xpath://*[@text='{FOLDER_NAME}']"
    ARTICLE_BY_TITLE_TPL = f"xpath://*[@text='{TITLE}']"
    TITLE_TOPIC_IN_LIST = f"xpath://*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Python (programming language)']"
    TITLE_DESCRIPTION_IN_LIST = f"xpath://*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='general-purpose programming language']"

    def get_folder_xpath_by_name(self, name_of_folder: str):
        return self.FOLDER_BY_NAME_TPL.replace(f"{self.FOLDER_NAME}", name_of_folder)

    def get_saved_article_xpath_by_title(self, article_title):
        return self.ARTICLE_BY_TITLE_TPL.replace(f"{self.TITLE}", article_title)

    def wait_for_article_to_appear_by_title(self, article_title: str):
        article_xpath = self.get_saved_article_xpath_by_title(article_title)
        self.wait_for_element_present(article_xpath,
                                      "Cannot find saved article by title " + article_title,
                                      15)

    def wait_for_article_to_disappear_by_title(self, article_title):
        article_xpath = self.get_saved_article_xpath_by_title(article_title)
        self.wait_for_element_not_present(article_xpath,
                                          "Saved article still present with title " + article_title,
                                          15)

    def assert_has_text(self):
        self.assert_element_has_text(self.TITLE_TOPIC_IN_LIST,
                                     "Python (programming language)",
                                     "Cannot title of topic after remove",
                                     5)

        self.assert_element_has_text(self.TITLE_DESCRIPTION_IN_LIST,
                                     "general-purpose programming language",
                                     "Cannot description of topic after remove",
                                     5)

    def click_on_article_from_the_list(self):
        self.wait_for_element_and_click(self.TITLE_DESCRIPTION_IN_LIST,
                                        "Cannot find element for redirect to reading list",
                                        6)

    def open_folder_by_name(self, name_of_folder):
        folder_name_xpath = self.get_folder_xpath_by_name(name_of_folder)
        self.wait_for_element_and_click(folder_name_xpath,
                                        "Cannot find folder by name" + name_of_folder,
                                        5)

    def swipe_by_article_to_delete(self, article_title):
        article_xpath = self.get_saved_article_xpath_by_title(article_title)
        self.wait_for_article_to_appear_by_title(article_title)
        self.swipe_element_to_left(article_xpath, "Cannot find saved article")
        self.wait_for_article_to_disappear_by_title(article_title)
