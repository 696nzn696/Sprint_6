import allure
import pytest

from locators.ordering_scooter_locators import OrderingScooterPageLocators
from locators.main_locators import MainPageLocators
from pages.ordering_scooter_page import OrderingScooterPage

class TestOrderingScooterPage:

    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str, days_text, color_name, comment_text",
                             [("Иван", "Иванов", "проспект Мира дом 33", "Сокольники", "79301234455", "31.08.2026", "трое суток", "чёрный жемчуг", "По прибытию перезвоните")])
    @allure.title('Проверка успешного заказа самоката через кнопку "Заказать" снизу страницы')
    def test_ordering_scooter_button_order_below(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        order_page = OrderingScooterPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.open_from_main_page(MainPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_element(OrderingScooterPageLocators.SUBMIT_BUTTON)
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_element(OrderingScooterPageLocators.ORDER_BUTTON_IN_FORM)
        message = order_page.complete_order_confirmation()
        assert "Заказ оформлен" in message


    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str, days_text, color_name, comment_text",
                             [("Иван", "Иванов", "проспект Мира дом 33", "Сокольники", "79301234455", "31.08.2026", "трое суток", "чёрный жемчуг", "По прибытию перезвоните")])
    @allure.title('Проверка успешного заказа самоката через кнопку "Заказать" сверху страницы')
    def test_ordering_scooter_button_order_on_top(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        order_page = OrderingScooterPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        order_page.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_element(OrderingScooterPageLocators.SUBMIT_BUTTON)
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_element(OrderingScooterPageLocators.ORDER_BUTTON_IN_FORM)
        message = order_page.complete_order_confirmation()
        assert "Заказ оформлен" in message

