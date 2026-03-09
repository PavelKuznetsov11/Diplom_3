from selenium.webdriver.common.by import By

class LoginPageLocators:

    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/..//input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(),'Пароль')]/..//input")
    ENTER_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

