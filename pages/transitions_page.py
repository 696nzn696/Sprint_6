import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

class TransitionsPage:

    def __init__(self, driver): 
        self.driver = driver

    @allure.step('Клик по логотипу "Самокат"')
    def click_logo_scooter(self):
        self.driver.find_element(*logo_scooter).click()

    @allure.step('Клик по логотипу "Яндекс"')
    def click_logo_yandex(self):
        self.driver.find_element(*logo_yandex).click()

    @allure.step('Ожидание появления главной страницы "Самокат"')
    def wait_url_scooter(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be((url_scooter)))

    @allure.step('Клик по кнопке "Заказать" вверху страницы')
    def click_button_order_on_top(self):
        self.driver.find_element(*button_order_on_top).click()

    @allure.step('Ожидание видимости формы заказа')
    def wait_order_form(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(name_field))

    @allure.step("Ожидание новой вкладки")
    def wait_for_new_tab(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1, message="После клика не появилась новая вкладка")

    @allure.step("Переключение на последнюю вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Содержание подстроки в URL текущей вкладки")
    def wait_url_contains(self, substring, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: substring in d.current_url, message=f"URL не содержит '{substring}'")

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    def page_transitions_scooter(self):
        self.click_button_order_on_top()
        self.wait_order_form()
        self.click_logo_scooter()
        return self.wait_url_scooter()

    def page_transitions_dzen(self):
        self.click_logo_yandex()
        self.wait_for_new_tab()
        self.switch_to_last_tab()
        self.wait_url_contains("dzen.ru")
        url = self.get_current_url()
        return url
