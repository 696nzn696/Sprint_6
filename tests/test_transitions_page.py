import allure
from locators import * 

class TestTransitionsPage:

    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_click_through_scooter(self, driver, transitions_page):
        transitions_page.page_transitions_scooter()
        assert driver.current_url == url_scooter

    @allure.title('Проверка перехода на страницу Дзена по клику на лого Яндекса')
    def test_click_through_yandex(self, transitions_page):
        result = transitions_page.page_transitions_dzen()
        assert "dzen.ru" in result
