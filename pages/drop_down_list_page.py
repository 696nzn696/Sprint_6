import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


class DropDownListPageScooter:

    def __init__(self, driver): 
        self.driver = driver

    @allure.step('Скролл в нижнюю часть страницы')
    def scroll_to_behind_MKAD(self):
        element = self.driver.find_element(*behind_MKAD)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание видимости самого нижнего элемента страницы')
    def wait_item_from_the_list(self, item):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(item))

    @allure.step('Клик по вопросу из раздела "Вопросы о важном"')
    def click_item_from_the_list(self, item):
        self.driver.find_element(*item).click()

    @allure.step('Проверка видимости выпадающего из списка ответа из раздела "Вопросы о важном"')
    def check_visibility_of_the_drop_down_list(self, drop_down):
        return self.driver.find_element(*drop_down).is_displayed()

    def drop_down_list(self, item, drop_down):
        self.scroll_to_behind_MKAD()
        self.wait_item_from_the_list(item)
        self.click_item_from_the_list(item)
        return self.check_visibility_of_the_drop_down_list(drop_down)
