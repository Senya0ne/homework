from src.ui.MyListsPageObject import MyListsPageObject
from src.ui.SearchPageObject import SearchPageObject
from src.ui.ArticlePageObject import ArticlePageObject


def test_search_element_after_remove_from_directory(driver):
    search_page_object = SearchPageObject(driver)
    search_page_object.init_search_input()
    search_page_object.type_search_line("Java")
    search_page_object.click_by_article_with_substring("Object-oriented programming language")

    article_page_object = ArticlePageObject(driver)
    article_page_object.wait_for_title_element()
    article_title = article_page_object.get_article_title()
    article_page_object.add_article_to_my_list()
    article_page_object.close_article()

    search_page_object.init_search_input()
    search_page_object.type_search_line("Python")
    search_page_object.click_by_article_with_substring("General-purpose programming language")
    article_page_object.wait_for_title_element()
    article_page_object.add_second_article_to_my_list()

    mylists_page_object = MyListsPageObject(driver)

    mylists_page_object.swipe_by_article_to_delete(article_title)
    mylists_page_object.wait_for_article_to_disappear_by_title(article_title)
    mylists_page_object.assert_has_text()
    mylists_page_object.click_on_article_from_the_list()

    article_page_object.wait_for_title_element()
    assert "Python (programming language)" == article_page_object.get_article_title()


def test_assert_has_present_title_for_topic(driver):
    search_page_object = SearchPageObject(driver)
    search_page_object.init_search_input()
    search_page_object.type_search_line("Java")
    search_page_object.click_by_article_with_substring("Object-oriented programming language")

    article_page_object = ArticlePageObject(driver)
    article_page_object.wait_for_title_element()
