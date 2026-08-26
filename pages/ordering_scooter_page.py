import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

class OrderingScooterPage:

    def __init__(self, driver): 
        self.driver = driver

    @allure.step('Ожидание видимости сообщения о куках')
    def wait_cookies(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(cookies))

    @allure.step('Клик по кнопке "да все привыкли" для закрытия куков')
    def click_button_cookies(self):
        self.driver.find_element(*cookies).click()

    @allure.step('Клик по кнопке "Заказать" вверху страницы')
    def click_button_order_on_top(self):
        self.driver.find_element(*button_order_on_top).click()

    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_button_order_below(self):
            self.driver.find_element(*button_order_below).click()

    @allure.step('Скролл до кнопки "Заказать" внизу страницы')
    def scroll_button_order_below(self):
        element = self.driver.find_element(*button_order_below)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание видимости формы заказа')
    def wait_order_form(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(name_field))

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.driver.find_element(*name_field).send_keys(name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_surname(self, surname):
        self.driver.find_element(*surname_field).send_keys(surname)

    @allure.step('Заполнение поля "Адрес: куда привезти заказ"')
    def set_addres_field(self, addres):
        self.driver.find_element(*addres_field).send_keys(addres)

    @allure.step('Клик по полю "Станция метро"')
    def click_subway_field(self):
        self.driver.find_element(*subway_field).click()

    @allure.step('Ожидание видимости выпадающего списка станций метро')
    def wait_subway_drop_down_list(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(subway_drop_down_list))

    @allure.step('Клик по станции метро "Сокольники"')
    def click_station(self):
        self.driver.find_element(*station).click()

    @allure.step('Заполнение поля "Телефон: на него позвонит курьер"')
    def set_telephone_field(self, telephone):
        self.driver.find_element(*telephone_field).send_keys(telephone)

    @allure.step('Клик по кнопке "Далее"')
    def click_button_further(self):
        self.driver.find_element(*button_further).click()

    @allure.step('Ожидание видимости формы "Про аренду"')
    def wait_about_rent(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(date_field))

    @allure.step('Клик по полю "Когда привезти самокат"')
    def click_date_field(self):
        self.driver.find_element(*date_field).click()

    @allure.step('Ожидание видимости выпадающей таблицы с календарем')
    def wait_date_table(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(date_table))

    @allure.step('Клик по дате')
    def click_date_option(self):
        self.driver.find_element(*date_option).click()

    @allure.step('Клик по полю "Срок аренды"')
    def click_tern_field(self):
        self.driver.find_element(*tern_field).click()

    @allure.step('Ожидание видимости выпадающего списка с сроками')
    def wait_tern_drop_down_list(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(tern_drop_down_list))

    @allure.step('Клик по сроку')
    def click_tern_option(self):
        self.driver.find_element(*tern_option).click()

    @allure.step('Клик по цвету "Чёрный жемчуг"')
    def click_colour_black(self):
        self.driver.find_element(*colour_black).click()

    @allure.step('Клик по кнопку "Заказать"')
    def click_button_order_finish(self):
        self.driver.find_element(*button_order_finish).click()

    @allure.step('Ожидание появления всплывающего окна с сообщением "Хотите оформить заказ?"')
    def wait_consent_to_making_an_order(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(confirming_response))

    @allure.step('Клик по кнопку "Да"')
    def click_button_yes(self):
        self.driver.find_element(*confirming_response).click()

    @allure.step("Ожидание сообщения 'Заказ оформлен' в всплывающем окне")
    def wait_for_success_popup(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(order_has_been_placed))

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_order_message(self):
        element = self.driver.find_element(*order_has_been_placed)
        return element.text.strip()



    def ordering_scooter_button_order_on_top(self, name="Иван", surname="Иванов", addres="проспект Мира дом 33", telephone="79301234455"):
        self.wait_cookies()
        self.click_button_cookies()
        self.click_button_order_on_top()
        self.wait_order_form()
        self.set_name(name)
        self.set_surname(surname)
        self.set_addres_field(addres)
        self.click_subway_field()
        self.wait_subway_drop_down_list()
        self.click_station()
        self.set_telephone_field(telephone)
        self.click_button_further()
        self.wait_about_rent()
        self.click_date_field()
        self.wait_date_table()
        self.click_date_option()
        self.click_tern_field()
        self.wait_tern_drop_down_list()
        self.click_tern_option()
        self.click_colour_black()
        self.click_button_order_finish()
        self.wait_consent_to_making_an_order()
        self.click_button_yes()
        self.wait_for_success_popup()
        return self.get_success_order_message()

    def ordering_scooter_button_order_below(self, name="Иван", surname="Иванов", addres="проспект Мира дом 33", telephone="79301234455"):
        self.wait_cookies()
        self.click_button_cookies()
        self.scroll_button_order_below()
        self.click_button_order_below()
        self.wait_order_form()
        self.set_name(name)
        self.set_surname(surname)
        self.set_addres_field(addres)
        self.click_subway_field()
        self.wait_subway_drop_down_list()
        self.click_station()
        self.set_telephone_field(telephone)
        self.click_button_further()
        self.wait_about_rent()
        self.click_date_field()
        self.wait_date_table()
        self.click_date_option()
        self.click_tern_field()
        self.wait_tern_drop_down_list()
        self.click_tern_option()
        self.click_colour_black()
        self.click_button_order_finish()
        self.wait_consent_to_making_an_order()
        self.click_button_yes()
        self.wait_for_success_popup()
        return self.get_success_order_message()

