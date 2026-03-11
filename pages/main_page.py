from locators.base_page_locators import BasePageLocators as BPL
from locators.constructor_page_locators import ConstructorPageLocators as CPL
from locators.feed_page_locators import FeedPageLocators as FPL
from locators.login_page_locators import LoginPageLocators as LPL
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage(BasePage):

    @allure.step("Переходим на вкладку лента заказов из вкладки конструктора")
    def click_feed_tab_from_constructor_tab(self):
        self.force_click_element(BPL.FEED_BUTTON)
        self.wait_element(FPL.FEED_TITLE)
        return self.get_element_text(FPL.FEED_TITLE)

    @allure.step("Скролим до нужного ингредиента и кликаем по нему")
    def click_ingredient(self):
        self.scroll_to_element(CPL.SAUCE_INGREDIENT)
        self.force_click_element(CPL.SAUCE_INGREDIENT)
        self.wait_element(CPL.DETAILS_INGREDIENT)
        return self.get_element_text(CPL.DETAILS_INGREDIENT)

    @allure.step("Закрываем попап с деталями ингредиента")
    def close_popup_details_ingredient(self):
        self.scroll_to_element(CPL.SAUCE_INGREDIENT)
        self.force_click_element(CPL.SAUCE_INGREDIENT)
        self.wait_element(CPL.DETAILS_INGREDIENT)
        self.force_click_element(CPL.CLOSE_BUTTON)
        self.wait_element(CPL.CONSTRUCTOR_TITLE)
        return self.get_element_text(CPL.CONSTRUCTOR_TITLE)
    
    @allure.step('Получить количество добавленных ингредиентов в корзину')
    def get_counter_text(self):
        return self.get_element_text(CPL.COUNTER)

    
    @allure.step('Переходим на вкладку конструктор')
    def click_constructor_tab_from_feed_page(self):
       self.force_click_element(BPL.CONSTRUCTOR_BUTTON)
       self.wait_element(CPL.CONSTRUCTOR_TITLE)
       return self.get_element_text(CPL.CONSTRUCTOR_TITLE)
    
    @allure.step('Переходим на вкладку лента заказов из вкладки конструктора')
    def change_tab_constructor_to_feed(self):
        self.force_click_element(BPL.FEED_BUTTON)
        self.wait_element(FPL.FEED_TITLE)

    @allure.step('Переходим на вкладку конструктор из вкладки лента заказов')
    def change_tab_feed_to_constructor(self):
        self.force_click_element(BPL.CONSTRUCTOR_BUTTON)
        self.wait_element(CPL.CONSTRUCTOR_TITLE)
    
    
    @allure.step('Получаем счетчик выполненных за все время заказов')
    def get_completed_all_time_orders(self):
        return self.get_element_text(FPL.COMPLETED_ALL_TIME_ORDERS)
    
    @allure.step('Получаем счетчик выполненных за сегодня заказов')
    def get_completed_today_orders(self):
        return self.get_element_text(FPL.COMPLETED_TODAY_ORDERS)
    
    @allure.step("Перетаскиваем ингредиент в корзину конструктора")
    def drag_ingredient_to_basket(self):
        self.scroll_to_element(CPL.BASKET_CONSTRUCTOR)
        self.drag_and_drop(
            CPL.BUN ,CPL.SAUCE_INGREDIENT, CPL.BASKET_CONSTRUCTOR)
        
    @allure.step('Вводим email в поле для ввода email')
    def input_email(self, email):
        self.find_element(LPL.EMAIL_INPUT).send_keys(email)

    @allure.step('Вводим пароль в поле для ввода пароля')
    def input_password(self, password):
        self.find_element(LPL.PASSWORD_INPUT).send_keys(password)

    @allure.step('Кликаем по кнопке войти')
    def click_enter_login_button(self):
        self.force_click_element(LPL.ENTER_LOGIN_BUTTON)
    
    @allure.step('Логинимся в систему')
    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_enter_login_button()

    @allure.step('Оформить заказ')
    def place_order(self):
        self.force_click_element(CPL.PLACE_ORDER_BUTTON)
        self.wait_order_number(CPL.ORDER_NUMBER)
        order_number = self.get_element_text(CPL.ORDER_NUMBER)
        self.force_click_element(CPL.CLOSE_BUTTON)
        self.wait_element(BPL.CONSTRUCTOR_BUTTON)
        return order_number
    
    @allure.step('Номер заказа появился в разделе "В работе"')
    def check_order_in_progress(self):
        self.wait_order_in_progress()
        return self.get_element_text(FPL.IN_PROGRESS_ORDERS)
    
    @allure.step('Счётчик "Выполнено за всё время" увеличивается')
    def check_all_time_order_counter(self, old_count):
        self.wait_counter(FPL.COMPLETED_ALL_TIME_ORDERS, old_count)
        return self.get_element_text(FPL.COMPLETED_ALL_TIME_ORDERS)
    
    @allure.step('Счётчик "Выполнено за сегодня" увеличивается')
    def check_today_order_counter(self, old_count):
        self.wait_counter(FPL.COMPLETED_TODAY_ORDERS, old_count)
        return self.get_element_text(FPL.COMPLETED_TODAY_ORDERS)
    
    @allure.step('Ожидание загрузки страницы Конструктор')
    def wait_constructor_page(self):
        self.wait_element(CPL.CONSTRUCTOR_TITLE)

    @allure.step('Ожидание загрузки страницы Лента заказов')
    def wait_feed_page(self):
        self.wait_element(FPL.FEED_TITLE)

