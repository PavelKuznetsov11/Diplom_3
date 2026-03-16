
import allure
from pages.main_page import MainPage
from data import Data

class TestSectionFeed:

    @allure.title('Проверка, что при создании нового заказа счётчик ' \
    '"Выполнено за все время" увеличивается,' \
    ' в браузере Google Chrome и Mozilla Firefox')
    def test_check_counter_completed_all_time_orders(self, login_page_driver):
        feed_page = MainPage(login_page_driver)
        feed_page.login(Data.EMAIL, Data.PASSWORD)
        feed_page.wait_constructor_page()
        feed_page.change_tab_constructor_to_feed()
        feed_page.wait_feed_page()
        old_count_all_orders = int(feed_page.get_completed_all_time_orders())
        feed_page.change_tab_feed_to_constructor()
        feed_page.drag_ingredient_to_basket()
        feed_page.place_order()
        feed_page.change_tab_constructor_to_feed()
        count_all_orders = feed_page.check_all_time_order_counter(old_count_all_orders)
        assert int(count_all_orders) > old_count_all_orders

    @allure.title('Проверка, что при создании нового заказа счётчик ' \
    '"Выполнено за сегодня" увеличивается,' \
    'в браузере Google Chrome и Mozilla Firefox')
    def test_check_counter_completed_today_orders(self, login_page_driver):
        feed_page = MainPage(login_page_driver)
        feed_page.login(Data.EMAIL, Data.PASSWORD)
        feed_page.wait_constructor_page()
        feed_page.change_tab_constructor_to_feed()
        feed_page.wait_feed_page()
        old_count_today_orders = int(feed_page.get_completed_today_orders())
        feed_page.change_tab_feed_to_constructor()
        feed_page.drag_ingredient_to_basket()
        feed_page.place_order()
        feed_page.change_tab_constructor_to_feed()
        count_today_orders = feed_page.check_today_order_counter(old_count_today_orders)
        assert int(count_today_orders) > old_count_today_orders

    @allure.title('Проверка, что при создании нового заказа' \
    ' номер заказа появляется в разделе "В работе" ' \
    'в браузере Google Chrome и Mozilla Firefox')
    def test_check_order_appears_in_progress_section(self, login_page_driver):
        feed_page = MainPage(login_page_driver)
        feed_page.login(Data.EMAIL, Data.PASSWORD)
        feed_page.wait_constructor_page()
        feed_page.drag_ingredient_to_basket()
        order_number = feed_page.place_order()
        feed_page.change_tab_constructor_to_feed()
        order_in_progress = feed_page.check_order_in_progress()
        assert order_number in order_in_progress


