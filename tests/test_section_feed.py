
import allure

from locators.base_page_locators import BasePageLocators as BPL
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.feed_page_locators import FeedPageLocators as FPL

from pages.main_page import MainPage

from data import Data

class TestSectionFeed:

    @allure.title('Проверка, что при создании нового заказа счётчики ' \
    '"Выполнено за все время" и "Выполнено за сегодня" увеличиваются,' \
    ' также номер заказа появляется в разделе "В работе" в браузере Google Chrome')
    def test_check_counter_completed_all_time_orders_chrome(self, login_page_chrome_driver):
        feed_page = MainPage(login_page_chrome_driver)
        feed_page.login(Data.EMAIL, Data.PASSWORD)
        feed_page.wait_element(CPL.CONSTRUCTOR_TITLE)
        feed_page.change_tab(BPL.FEED_BUTTON, FPL.FEED_TITLE)
        feed_page.wait_element(FPL.FEED_TITLE)
        old_count_all_orders = int(feed_page.get_completed_all_time_orders())
        old_count_today_orders = int(feed_page.get_completed_today_orders())
        feed_page.change_tab(BPL.CONSTRUCTOR_BUTTON, CPL.CONSTRUCTOR_TITLE)
        feed_page.drag_ingredient_to_basket()
        order_number = feed_page.place_order()
        feed_page.change_tab(BPL.FEED_BUTTON, FPL.FEED_TITLE)
        order_in_progress = feed_page.check_order_in_progress()
        count_all_orders = feed_page.check_all_time_order_counter(old_count_all_orders)
        count_today_orders = feed_page.check_today_order_counter(old_count_today_orders)
        assert order_number in order_in_progress
        assert int(count_all_orders) > old_count_all_orders
        assert int(count_today_orders) > old_count_today_orders

    @allure.title('Проверка, что при создании нового заказа счётчики ' \
    '"Выполнено за все время" и "Выполнено за сегодня" увеличиваются,' \
    ' также номер заказа появляется в разделе "В работе" в браузере Mozilla Firefox')
    def test_check_counter_completed_all_time_orders_firefox(self, login_page_firefox_driver):
        feed_page = MainPage(login_page_firefox_driver)
        feed_page.login(Data.EMAIL, Data.PASSWORD)
        feed_page.wait_element(CPL.CONSTRUCTOR_TITLE)
        feed_page.change_tab(BPL.FEED_BUTTON, FPL.FEED_TITLE)
        feed_page.wait_element(FPL.FEED_TITLE)
        old_count_all_orders = int(feed_page.get_completed_all_time_orders())
        old_count_today_orders = int(feed_page.get_completed_today_orders())
        feed_page.change_tab(BPL.CONSTRUCTOR_BUTTON, CPL.CONSTRUCTOR_TITLE)
        feed_page.drag_ingredient_to_basket()
        order_number = feed_page.place_order()
        feed_page.change_tab(BPL.FEED_BUTTON, FPL.FEED_TITLE)
        order_in_progress = feed_page.check_order_in_progress()
        count_all_orders = feed_page.check_all_time_order_counter(old_count_all_orders)
        count_today_orders = feed_page.check_today_order_counter(old_count_today_orders)
        assert order_number in order_in_progress
        assert int(count_all_orders) > old_count_all_orders
        assert int(count_today_orders) > old_count_today_orders

