import pytest
import allure
from locators import * 


class TestDropDownListPage:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('На странице ищем выпадающий список и проверям, что при клике на каждый вопрос открывается ответ на него')
    @pytest.mark.parametrize('item,drop_down', [
        (cost, cost_expanded), 
        (multiple_scooters, multiple_scooters_expanded), 
        (time, time_expanded),
        (scooter_today, scooter_today_expanded),
        (renewal_and_refunds, renewal_and_refunds_expanded),
        (charging, charging_expanded),
        (cancellation, cancellation_expanded),
        (behind_MKAD, behind_MKAD_expanded)
    ])
    def test_drop_down_list_cost(self, drop_down_list_page, item, drop_down):
        result = drop_down_list_page.drop_down_list(item, drop_down)
        assert result
