import allure

from locators.transitions_locators import TransitionsPageLocators
from pages.base_page import BasePage

class TransitionsPage(BasePage):

    @allure.step("Клик по лого Самокат")
    def click_scooter_logo(self):
        click_logo = self.click_element(TransitionsPageLocators.SCOOTER_LOGO)
        return click_logo

    @allure.step("Клик по лого Яндекс")
    def click_yandex_logo(self):
        click_logo = self.click_element(TransitionsPageLocators.YANDEX_LOGO)
        return click_logo