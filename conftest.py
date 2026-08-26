import pytest
from selenium import webdriver
from pages.drop_down_list_page import DropDownListPageScooter
from pages.ordering_scooter_page import OrderingScooterPage
from pages.transitions_page import TransitionsPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def base_url():
    return 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture(scope="function")
def drop_down_list_page(driver, base_url):
    driver.get(base_url)
    page = DropDownListPageScooter(driver)
    return page

@pytest.fixture(scope="function")
def ordering_scooter_page(driver, base_url):
    driver.get(base_url)
    page = OrderingScooterPage(driver)
    return page

@pytest.fixture(scope="function")
def transitions_page(driver, base_url):
    driver.get(base_url)
    page = TransitionsPage(driver)
    return page
