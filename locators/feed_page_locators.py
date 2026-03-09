from selenium.webdriver.common.by import By

class FeedPageLocators:

    FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    COMPLETED_ALL_TIME_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    COMPLETED_TODAY_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    IN_PROGRESS_ORDERS = (By.XPATH, '//ul[contains(@class, "orderListReady")]/li') 

