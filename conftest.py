import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture
def create_driver_chrome():
    driver_chrome = webdriver.Chrome()
    driver_chrome.maximize_window()

    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture
def create_driver_firefox():
    driver_firefox = webdriver.Firefox()
    driver_firefox.maximize_window()

    yield driver_firefox
    driver_firefox.quit()


@pytest.fixture
def constructor_page_chrome_driver(create_driver_chrome):
    create_driver_chrome.get(Urls.HOME_URL)
    return create_driver_chrome


@pytest.fixture
def constructor_page_firefox_driver(create_driver_firefox):
    create_driver_firefox.get(Urls.HOME_URL)
    return create_driver_firefox


@pytest.fixture
def feed_page_chrome_driver(create_driver_chrome):
    create_driver_chrome.get(Urls.FEED_URL)
    return create_driver_chrome


@pytest.fixture
def feed_page_firefox_driver(create_driver_firefox):
    create_driver_firefox.get(Urls.FEED_URL)
    return create_driver_firefox


@pytest.fixture
def login_page_chrome_driver(create_driver_chrome):
    create_driver_chrome.get(Urls.LOGIN_URL)
    return create_driver_chrome


@pytest.fixture
def login_page_firefox_driver(create_driver_firefox):
    create_driver_firefox.get(Urls.LOGIN_URL)
    return create_driver_firefox

