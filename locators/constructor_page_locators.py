from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')
    SAUCES_TAB = (By.XPATH, '//span[text()="Соусы"]')
    SAUCE_INGREDIENT = (By.XPATH, '//img[contains(@alt,"Плоды Фалленианского дерева") '
    'and contains(@class,"BurgerIngredient")]/ancestor::a')
    BUN = (By.XPATH, '//img[contains(@alt,"Краторная булка N-200i") '
    'and contains(@class,"BurgerIngredient")]/ancestor::a')
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "close")]')
    DETAILS_INGREDIENT = (By.XPATH, '//h2[text()="Детали ингредиента"]') 
    FILLINGS_TAB = (By.XPATH, '//span[text()="Начинки"]')
    BASKET_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class, "BurgerConstructor")]')
    COUNTER = (By.XPATH, '//p[contains(text(),"Плоды Фалленианского дерева") '
    'and contains(@class,"BurgerIngredient")]'
    '/preceding-sibling::div[contains(@class,"counter")]/p')
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "title")]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

