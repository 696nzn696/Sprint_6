import pytest
import allure

from locators.drop_down_list_locators import DropDownPageLocators
from pages.drop_down_list_page import DropDownListPageScooter



class TestDropDownListPage:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('На странице ищем выпадающий список и проверям, что при клике на каждый вопрос открывается точный ответ на него')
    @pytest.mark.parametrize('question_locator,answer_locator, expected_text',
                             [(DropDownPageLocators.QUESTION_COST, DropDownPageLocators.ANSWER_COST, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                              (DropDownPageLocators.QUESTION_MULTIPLE_ORDERS, DropDownPageLocators.ANSWER_MULTIPLE_ORDERS, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                              (DropDownPageLocators.QUESTION_RENTAL_TIME, DropDownPageLocators.ANSWER_RENTAL_TIME, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                              (DropDownPageLocators.QUESTION_ORDER_TODAY, DropDownPageLocators.ANSWER_ORDER_TODAY, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                              (DropDownPageLocators.QUESTION_ORDER_EXTENSION, DropDownPageLocators.ANSWER_ORDER_EXTENSION, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                              (DropDownPageLocators.QUESTION_CHARGER, DropDownPageLocators.ANSWER_CHARGER, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                              (DropDownPageLocators.QUESTION_ORDER_CANCELLATION, DropDownPageLocators.ANSWER_ORDER_CANCELLATION, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                              (DropDownPageLocators.QUESTION_DELIVERY_OUTSIDE_MKAD, DropDownPageLocators.ANSWER_DELIVERY_OUTSIDE_MKAD, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
                              ],
                              ids = [
                                  "cost",
                                  "multiple_orders",
                                  "rental_time",
                                  "order_today",
                                  "order_extension",
                                  "charger",
                                  "order_cancellation",
                                  "delivery_outside_mkad"
                              ]
                              )
    
    def test_drop_down_list_cost(self, driver, question_locator, answer_locator, expected_text):
        faq_page = DropDownListPageScooter(driver)
        faq_page.open()
        faq_page.accept_cookies()
        faq_page.scroll_to_element(DropDownPageLocators.FAQ_SECTION)
        faq_page.open_question_and_wait_answer(question_locator, answer_locator)
        answer_text = faq_page.get_text_from_element(answer_locator)
        assert answer_text == expected_text
