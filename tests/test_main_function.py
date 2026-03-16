
import allure
from pages.main_page import MainPage
from data import Data

class TestMainFunction:

    @allure.title('Смена страницы с ленты заказов на конструктор в браузере ' \
    'Google Chrome и Mozilla Firefox')
    def test_move_constructor_tab_from_feed_tab(self, feed_page_driver):
        feed_page = MainPage(feed_page_driver)
        title = feed_page.click_constructor_tab_from_feed_page()
        assert title == Data.CONSTRUCTOR_TITLE, Data.CONSTRUCTOR_TITLE_ERROR

    @allure.title('Смена страницы с конструктора на ленту заказов в браузере ' \
    'Google Chrome и Mozilla Firefox')
    def test_move_feed_tab_from_constructor_tab(self, constructor_page_driver):
        constructor_page = MainPage(constructor_page_driver)
        title = constructor_page.click_feed_tab_from_constructor_tab()
        assert title == Data.FEED_TITLE, Data.FEED_TITLE_ERROR

    @allure.title('Клик по ингредиенту в конструкторе в браузере ' \
    'Google Chrome и Mozilla Firefox')
    def test_click_sauce_ingredient(self, constructor_page_driver):
        constructor_page = MainPage(constructor_page_driver)
        ingredient = constructor_page.click_ingredient()
        assert ingredient == Data.DETAILS_INGREDIENT, Data.DETAILS_INGREDIENT_ERROR

    @allure.title('Закрытие попапа с деталями ингредиента в конструкторе в браузере ' \
    'Google Chrome и Mozilla Firefox')
    def test_close_popup_details_ingredient_page(self, constructor_page_driver):
        constructor_page = MainPage(constructor_page_driver)
        title = constructor_page.close_popup_details_ingredient()
        assert title == Data.CONSTRUCTOR_TITLE, Data.POPUP_CLOSE_ERROR

    @allure.title('Перетаскивание ингредиентов в корзину конструктора в браузере ' \
    'Google Chrome и Mozilla Firefox')
    def test_drag_ingredients_to_basket(self, constructor_page_driver):
        constructor_page = MainPage(constructor_page_driver)
        constructor_page.drag_ingredient_to_basket()
        counter = constructor_page.get_counter_text()
        assert counter == Data.COUNT_INGREDIENT, Data.DRAG_AND_DROP_ERROR



