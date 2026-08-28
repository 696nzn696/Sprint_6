import allure
import pytest

from locators.ordering_scooter_locators import OrderingScooterPageLocators
from locators.main_locators import MainPageLocators
from pages.ordering_scooter_page import OrderingScooterPage
from data.ordering_scooter_data import VALID_ORDER_DATA

class TestOrderingScooterPage:

    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str,days_text,color_name,comment_text", [tuple(VALID_ORDER_DATA.values())])
    @allure.title('Проверка успешного заказа самоката через кнопку "Заказать" снизу страницы')
    def test_ordering_scooter_button_order_below(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        order_page = OrderingScooterPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.open_form_header_order_button()
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_submit_button()
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_order_button_in_form()
        message = order_page.complete_order_confirmation()
        assert "Заказ оформлен" in message


    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str,days_text,color_name,comment_text", [tuple(VALID_ORDER_DATA.values())])
    @allure.title('Проверка успешного заказа самоката через кнопку "Заказать" сверху страницы')
    def test_ordering_scooter_button_order_on_top(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        order_page = OrderingScooterPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.scroll_to_bottom_order_button()
        order_page.click_bottom_order_button()
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_submit_button()
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_order_button_in_form()
        message = order_page.complete_order_confirmation()
        assert "Заказ оформлен" in message

