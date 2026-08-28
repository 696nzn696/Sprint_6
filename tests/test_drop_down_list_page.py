import pytest
import allure

from locators.drop_down_list_locators import DropDownPageLocators
from pages.drop_down_list_page import DropDownListPageScooter
from data.drop_down_list_data import FAQ_ANSWERS



class TestDropDownListPage:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('На странице ищем выпадающий список и проверям, что при клике на каждый вопрос открывается точный ответ на него')
    @pytest.mark.parametrize('question_locator,answer_locator,expected_text',
        [
            (DropDownPageLocators.QUESTION_COST, DropDownPageLocators.ANSWER_COST, FAQ_ANSWERS["cost"]),
            (DropDownPageLocators.QUESTION_MULTIPLE_ORDERS, DropDownPageLocators.ANSWER_MULTIPLE_ORDERS, FAQ_ANSWERS["multiple_orders"]),
            (DropDownPageLocators.QUESTION_RENTAL_TIME, DropDownPageLocators.ANSWER_RENTAL_TIME, FAQ_ANSWERS["rental_time"]),
            (DropDownPageLocators.QUESTION_ORDER_TODAY, DropDownPageLocators.ANSWER_ORDER_TODAY, FAQ_ANSWERS["order_today"]),
            (DropDownPageLocators.QUESTION_ORDER_EXTENSION, DropDownPageLocators.ANSWER_ORDER_EXTENSION, FAQ_ANSWERS["order_extension"]),
            (DropDownPageLocators.QUESTION_CHARGER, DropDownPageLocators.ANSWER_CHARGER, FAQ_ANSWERS["charger"]),
            (DropDownPageLocators.QUESTION_ORDER_CANCELLATION, DropDownPageLocators.ANSWER_ORDER_CANCELLATION, FAQ_ANSWERS["order_cancellation"]),
            (DropDownPageLocators.QUESTION_DELIVERY_OUTSIDE_MKAD, DropDownPageLocators.ANSWER_DELIVERY_OUTSIDE_MKAD, FAQ_ANSWERS["delivery_outside_mkad"])
        ],
        ids=[
            "cost",
            "multiple_orders",
            "rental_time",
            "order_today",
            "order_extension",
            "charger",
            "order_cancellation",
            "delivery_outside_mkad"
        ])
    
    def test_drop_down_list_cost(self, driver, question_locator, answer_locator, expected_text):
        faq_page = DropDownListPageScooter(driver)
        faq_page.open()
        faq_page.accept_cookies()
        faq_page.scroll_to_element(DropDownPageLocators.FAQ_SECTION)
        faq_page.open_question_and_wait_answer(question_locator, answer_locator)
        answer_text = faq_page.get_text_from_element(answer_locator)
        assert answer_text == expected_text
