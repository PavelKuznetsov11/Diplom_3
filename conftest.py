import pytest
from selenium import webdriver
from urls import Urls
from data import Data


@pytest.fixture(params=[Data.CHROME, Data.FIREFOX])
def create_driver(request):

    browser = request.param
    if browser == Data.CHROME:
        driver = webdriver.Chrome()
        driver.maximize_window()
    else:
        driver = webdriver.Firefox()
        driver.maximize_window()

    yield driver
    driver.quit()



@pytest.fixture
def constructor_page_driver(create_driver):
    create_driver.get(Urls.HOME_URL)
    return create_driver



@pytest.fixture
def feed_page_driver(create_driver):
    create_driver.get(Urls.FEED_URL)
    return create_driver


@pytest.fixture
def login_page_driver(create_driver):
    create_driver.get(Urls.LOGIN_URL)
    return create_driver

