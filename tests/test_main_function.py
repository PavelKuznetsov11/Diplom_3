
import allure

from locators.constructor_page_locators import ConstructorPageLocators as CPL

from pages.main_page import MainPage



class TestMainFunction:

    @allure.title('Смена страницы с ленты заказов на конструктор в браузере Google Chrome')
    def test_move_constructor_tab_from_feed_tab_chrome(self, feed_page_chrome_driver):
        feed_page = MainPage(feed_page_chrome_driver)
        title = feed_page.click_constructor_tab_from_feed_page()
        assert title == 'Соберите бургер', 'Переход на вкладку конструктора не произошел'

    @allure.title('Смена страницы с ленты заказов на конструктор в браузере Mozilla Firefox')
    def test_move_constructor_tab_from_feed_tab_firefox(self, feed_page_firefox_driver):
        feed_page = MainPage(feed_page_firefox_driver)
        title = feed_page.click_constructor_tab_from_feed_page()
        assert title == 'Соберите бургер', 'Переход на вкладку конструктора не произошел'

    @allure.title('Смена страницы с конструктора на ленту заказов в браузере Google Chrome')
    def test_move_feed_tab_from_constructor_tab_chrome(self, constructor_page_chrome_driver):
        constructor_page = MainPage(constructor_page_chrome_driver)
        title = constructor_page.click_feed_tab_from_constructor_tab()
        assert title == 'Лента заказов', 'Переход на вкладку лента заказов не произошел'

    @allure.title('Смена страницы с конструктора на ленту заказов в браузере Mozilla Firefox')
    def test_move_feed_tab_from_constructor_tab_firefox(self, constructor_page_firefox_driver):
        constructor_page = MainPage(constructor_page_firefox_driver)
        title = constructor_page.click_feed_tab_from_constructor_tab()
        assert title == 'Лента заказов', 'Переход на вкладку лента заказов не произошел'

    @allure.title('Клик по ингредиенту в конструкторе в браузере Google Chrome')
    def test_click_sauce_ingredient_chrome(self, constructor_page_chrome_driver):
        constructor_page = MainPage(constructor_page_chrome_driver)
        ingredient = constructor_page.click_ingredient()
        assert ingredient == 'Детали ингредиента', 'Окно с деталями ингредиента не открылось'

    @allure.title('Клик по ингредиенту в конструкторе в браузере Mozilla Firefox')
    def test_click_sauce_ingredient_firefox(self, constructor_page_firefox_driver):
        constructor_page = MainPage(constructor_page_firefox_driver)
        ingredient = constructor_page.click_ingredient()
        assert ingredient == 'Детали ингредиента', 'Окно с деталями ингредиента не открылось'

    @allure.title('Закрытие попапа с деталями ингредиента в конструкторе в браузере Google Chrome')
    def test_close_popup_details_ingredient_page_chrome(self, constructor_page_chrome_driver):
        constructor_page = MainPage(constructor_page_chrome_driver)
        title = constructor_page.close_popup_details_ingredient()
        assert title == 'Соберите бургер', 'Попап с деталями ингредиента не закрылся'

    @allure.title('Закрытие попапа с деталями ингредиента в конструкторе в браузере Mozilla Firefox')
    def test_close_popup_details_ingredient_page_firefox(self, constructor_page_firefox_driver):
        constructor_page = MainPage(constructor_page_firefox_driver)
        title = constructor_page.close_popup_details_ingredient()
        assert title == 'Соберите бургер', 'Попап с деталями ингредиента не закрылся'

    @allure.title('Перетаскивание ингредиентов в корзину конструктора в браузере Google Chrome')
    def test_drag_ingredients_to_basket_chrome(self, constructor_page_chrome_driver):
        constructor_page = MainPage(constructor_page_chrome_driver)
        constructor_page.drag_ingredient_to_basket()
        counter = constructor_page.get_element_text(CPL.COUNTER)
        assert counter == '1', 'Ингредиент не перетаскивается в корзину конструктора'

    @allure.title('Перетаскивание ингредиентов в корзину конструктора в браузере Mozilla Firefox')
    def test_drag_ingredients_to_basket_firefox(self, constructor_page_firefox_driver):
        constructor_page = MainPage(constructor_page_firefox_driver)
        constructor_page.drag_ingredient_to_basket()
        counter = constructor_page.get_element_text(CPL.COUNTER)
        assert counter == '1', 'Ингредиент не перетаскивается в корзину конструктора'

