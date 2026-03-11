from locators.base_page_locators import BasePageLocators as BPL
from locators.login_page_locators import LoginPageLocators as LPL
from locators.feed_page_locators import FeedPageLocators as FPL
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
import allure

class BasePage:

    @allure.step("Инициализация драйвера")
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент на странице')
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Заполяем поле на странице')
    def fill_field(self, locator, value):
        element = self.find_element(locator)
        element.send_keys(value)
        
    
    @allure.step('Ожиданием элемент')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Принудительный клик по элементу на странице')
    def force_click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step('Получаем текст заголовка страницы')
    def get_element_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)   

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop(self, bun_locator, ingredient_locator, target_locator):

        source1 = self.find_element(bun_locator)
        source2 = self.find_element(ingredient_locator)
        target = self.find_element(target_locator)

        for source in [source1, source2]:
            self.driver.execute_script(
                """
                var source = arguments[0];
                var target = arguments[1];
                var dt = new DataTransfer();
                source.dispatchEvent(new DragEvent('dragstart', {dataTransfer: dt, bubbles: true}));
                target.dispatchEvent(new DragEvent('drop', {dataTransfer: dt, bubbles: true}));
                source.dispatchEvent(new DragEvent('dragend', {dataTransfer: dt, bubbles: true}));
                """,
                source,
                target,
            )
        

    @allure.step('Ожидаем появление номера заказа в разделе "В работе"')
    def wait_order_in_progress(self):
        WebDriverWait(self.driver, 30).until(
    lambda driver:  driver.find_element(*FPL.IN_PROGRESS_ORDERS).text.strip().isdigit()
        )    


    @allure.step('После создания заказа счётчик увеличевается')
    def wait_counter(self, counter_locator, old_count):
        WebDriverWait(self.driver, 20).until(
    lambda d: int(d.find_element(*counter_locator).text) > int(old_count)
)
    
    @allure.step('Ожидаем номер заказа')
    def wait_order_number(self, locator):
        WebDriverWait(self.driver, 20).until(
    lambda d: len(d.find_element(*locator).text.strip()) > 4 
)





    

            