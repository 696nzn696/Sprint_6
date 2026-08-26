import allure
from locators import * 

class TestOrderingScooterPage:

    @allure.title('Проверка успешного заказа самоката через кнопку "Заказать" снизу страницы')
    def test_ordering_scooter_button_order_below(self, ordering_scooter_page):
        result = ordering_scooter_page.ordering_scooter_button_order_below()
        assert "Заказ оформлен" in result

    @allure.title('Проверка успешного заказа самоката через кнопку "Заказать" сверху страницы')
    def test_ordering_scooter_button_order_on_top(self, ordering_scooter_page):
        result = ordering_scooter_page.ordering_scooter_button_order_on_top()
        assert "Заказ оформлен" in result

