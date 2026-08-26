from selenium.webdriver.common.by import By

# ЛОКАТОРЫ ДЛЯ ПРОВЕРКИ ВЫПАДАЮЩЕГО СПИСКА 
cost = (By.ID, 'accordion__heading-0')
cost_expanded = (By.ID, 'accordion__panel-0')
multiple_scooters = (By.ID, 'accordion__heading-1')
multiple_scooters_expanded = (By.ID, 'accordion__panel-1')
time = (By.ID, 'accordion__heading-2')
time_expanded = (By.ID, 'accordion__panel-2')
scooter_today = (By.ID, 'accordion__heading-3')
scooter_today_expanded = (By.ID, 'accordion__panel-3')
renewal_and_refunds = (By.ID, 'accordion__heading-4')
renewal_and_refunds_expanded = (By.ID, 'accordion__panel-4')
charging = (By.ID, 'accordion__heading-5')
charging_expanded = (By.ID, 'accordion__panel-5')
cancellation = (By.ID, 'accordion__heading-6')
cancellation_expanded = (By.ID, 'accordion__panel-6')
behind_MKAD = (By.ID, 'accordion__heading-7')
behind_MKAD_expanded = (By.ID, 'accordion__panel-7')

# ЛОКАТОРЫ ДЛЯ ПРОВЕРКИ СЦЕНАРИЯ ЗАКАЗА САМОКАТА
# Куки
cookies = (By.ID, "rcc-confirm-button")
# Кнопки "Заказать"
button_order_on_top = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
button_order_below = (By.XPATH, "//button[contains(@class, 'Button_Middle')]")
# Форма заказа
name_field = (By.XPATH, "//input[@placeholder='* Имя']")
surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
addres_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
subway_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
subway_drop_down_list = ((By.CLASS_NAME, 'select-search__select'))
station = (By.XPATH, "//div[text()='Сокольники']")
telephone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
button_further = (By.XPATH, "//button[contains(text(), 'Далее')]")
# Форма "Про аренду"
date_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
date_table = (By.CLASS_NAME, "react-datepicker-popper")
date_option = (By.XPATH, '//div[@aria-label="Choose понедельник, 31-е августа 2026 г."]')
tern_field = (By.CLASS_NAME, "Dropdown-control")
tern_drop_down_list = (By.CLASS_NAME, "Dropdown-menu")
tern_option = (By.XPATH, "//div[text()='трое суток']")
colour_black = (By.XPATH, "//label[@for='black']")
button_order_finish = (By.XPATH, "//button[text()='Заказать' and contains(@class,'Button_Middle')]")
# Всплывающее окно "Хотите оформить заказ?"
confirming_response = (By.XPATH, "//button[contains(text(), 'Да')]")
# Всплывающее окно "Заказ оформлен"
order_has_been_placed = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")

# ЛОГОТИПЫ
logo_scooter = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
logo_yandex = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

# URL
url_scooter = "https://qa-scooter.praktikum-services.ru/"

