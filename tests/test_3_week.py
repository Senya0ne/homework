from src.ui.MainPageObject import MainPageObject
from selenium.webdriver.common.by import By


def test_search_element_after_remove_from_directory(driver):
    driver = MainPageObject(driver)
    driver.wait_for_element_and_click((By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
                                      "Cannot find search Wikipedia input", 5)
    driver.wait_for_element_and_send_keys((By.XPATH, "//*[contains(@text, 'Search…')]"), "Java",
                                          "Cannot find search input", 5)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Object-oriented programming language']"),
                                      "Cannot find 'Object-oriented programming language' topic searching by 'Java'",
                                      5)
    driver.wait_for_element_present((By.ID,
                                     "org.wikipedia:id/view_page_title_text"),
                                    "Cannot find article",
                                    15)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//android.widget.ImageView[@content-desc='More options']"),
                                      "Cannot find button to open article options",
                                      15)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//*[@text='Add to reading list']"),
                                      "Cannot find option to add article to reading list",
                                      15)
    driver.wait_for_element_and_click((By.ID,
                                       "org.wikipedia:id/onboarding_button"),
                                      "Cannot find 'GOT IT' tip overlay",
                                      15)
    driver.wait_for_element_and_clear((By.ID,
                                       "org.wikipedia:id/text_input"),
                                      "Cannot find input to set name of articles folder",
                                      15)
    name_of_folder = "Learning Programming"
    driver.wait_for_element_and_send_keys((By.ID, "org.wikipedia:id/text_input"),
                                          name_of_folder,
                                          "Cannot put text into articles folder input",
                                          5)
    driver.wait_for_element_and_click((By.XPATH, "//*[@text='OK']"),
                                      "Cannot press OK button",
                                      5)
    driver.wait_for_element_and_click((By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"),
                                      "Cannot close article, cannot find x link",
                                      5)

    driver.wait_for_element_and_click((By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
                                      "Cannot find search Wikipedia input", 5)
    driver.wait_for_element_and_send_keys((By.XPATH, "//*[contains(@text, 'Search…')]"), "Python",
                                          "Cannot find search input", 5)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='General-purpose programming language']"),
                                      "Cannot find 'Object-oriented programming language' topic searching by 'Python'",
                                      5)
    driver.wait_for_element_present((By.ID,
                                     "org.wikipedia:id/view_page_title_text"),
                                    "Cannot find article",
                                    15)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//android.widget.ImageView[@content-desc='More options']"),
                                      "Cannot find button to open article options",
                                      15)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//*[@text='Add to reading list']"),
                                      "Cannot find option to add article to reading list",
                                      15)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//*[@resource-id='org.wikipedia:id/item_container']//*[@text='Learning Programming']"),
                                      "Cannot find option to add article to reading list",
                                      15)
    driver.wait_for_element_and_click((By.ID, "org.wikipedia:id/snackbar_action"),
                                      "Cannot find element for redirect to rading list",
                                      6)

    driver.swipe_element_to_left((By.XPATH, "//*[@text='Java (programming language)']"),
                                 "Cannot find saved article")
    driver.wait_for_element_not_present((By.XPATH, "//*[@text='Java (programming language)']"),
                                        "Cannot delete saved article", 5)
    driver.assert_element_has_text((By.XPATH,
                                    "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Python (programming language)']"),
                                   "Python (programming language)",
                                   "Cannot title of topic after remove",
                                   5)
    driver.assert_element_has_text((By.XPATH,
                                    "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='general-purpose programming language']"),
                                   "general-purpose programming language",
                                   "Cannot description of topic after remove",
                                   5)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='general-purpose programming language']"),
                                      "Cannot find element for redirect to reading list",
                                      6)
    driver.wait_for_element_present((By.ID,
                                     "org.wikipedia:id/view_page_title_text"),
                                    "Cannot find title for Python article",
                                    15)


def test_assert_has_present_title_for_topic(driver):
    driver = MainPageObject(driver)
    driver.wait_for_element_and_click((By.XPATH, "//*[contains(@text,'Search Wikipedia')]"),
                                      "Cannot find search Wikipedia input", 5)
    driver.wait_for_element_and_send_keys((By.XPATH, "//*[contains(@text, 'Search…')]"), "Java",
                                          "Cannot find search input", 5)
    driver.wait_for_element_and_click((By.XPATH,
                                       "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Object-oriented programming language']"),
                                      "Cannot find 'Object-oriented programming language' topic searching by 'Java'",
                                      5)
    driver.assert_element_present((By.ID,
                                   "org.wikipedia:id/view_page_title_text"),
                                  "Cannot find title for article")
