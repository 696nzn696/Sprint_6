import allure

from locators.main_locators import MainPageLocators
from url import MAIN_URL
from pages.base_page import BasePage
from pages.transitions_page import TransitionsPage

class TestTransitionsPage:

    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_click_through_scooter(self, driver):
        order_page = BasePage(driver)
        transitions_page = TransitionsPage(driver)
        order_page.open()
        order_page.accept_cookies()
        transitions_page.click_scooter_logo()
        assert order_page.is_on_main_page(MAIN_URL), (f"Ожидался переход на {MAIN_URL}, но текущий URL: {order_page.get_current_url()}")

    @allure.title('Проверка перехода на страницу Дзена по клику на лого Яндекса')
    def test_click_through_yandex(self,driver):
        order_page = BasePage(driver)
        transitions_page = TransitionsPage(driver)
        order_page.open()
        order_page.accept_cookies()
        transitions_page.click_yandex_logo()
        order_page.wait_for_new_tab()
        order_page.switch_to_last_tab()
        order_page.wait_url_contains("dzen.ru")
        assert "dzen.ru" in order_page.get_current_url()