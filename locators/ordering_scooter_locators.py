from selenium.webdriver.common.by import By


class OrderingScooterPageLocators:
    # Поля формы заказа
    ORDER_FORM = (By.XPATH, ".//div[contains(@class, 'Order_Form')]") # Форма заказа
    NAME_FIELD = (By.XPATH, './/input[contains(@placeholder, "Имя")]') # Поле "Имя"
    SURNAME_FIELD = (By.XPATH, './/input[contains(@placeholder, "Фамилия")]') # Поле "Фамилия"
    ADDRESS_FIELD = (By.XPATH, './/input[contains(@placeholder, "Адрес")]') # Поле "Адрес"
    METRO_STATION_FIELD = (By.XPATH, './/input[contains(@placeholder, "метро")]') # Поле "Станция метро"
    METRO_OPTIONS = (By.XPATH, './/input[contains(@placeholder, "метро")]/ancestor::div//ul') # Список станций
    PHONE_NUMBER_FIELD = (By.XPATH, './/input[contains(@placeholder, "Телефон")]') # Поле "Телефон"
    SUBMIT_BUTTON = (By.XPATH, ".//button[(text() = 'Далее')]") # Кнопка "Далее"

    # Поля формы "Про аренду"
    DATE_FIELD = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]') # Поле "Дата"
    RENTAL_PERIOD_FIELD = (By.XPATH, ".//div[contains(text(), 'Срок аренды')]") # Срок аренды
    DAYS_OPTIONS = (By.CSS_SELECTOR, ".Dropdown-menu") # Список срока аренды
    COLOR_BLACK = (By.ID, "black") # Кнопка - черный цвет
    COLOR_GREY = (By.ID, "grey") # Кнопка - серый цвет
    ORDER_COMMENT = (By.XPATH,'.//input[@placeholder="Комментарий для курьера"]') # Поле "Комментарий"
    ORDER_BUTTON_IN_FORM = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[contains(text(), 'Заказать')]") # Кнопка "Заказать" в форме заказа

    # Всплывающее окно "Хотите оформить заказ?"
    YES_BUTTON = (By.XPATH, './/button[contains(text(), "Да")]') # Кнопка "Да"
    SUCCESS_ORDER_MESSAGE = (By.XPATH, ".//div[(text() = 'Заказ оформлен')]") # Сообщение об успешном оформлении заказа

    # Всплывающее окно "Заказ оформлен"
    ORDER_STATUS_BUTTON = (By.XPATH, './/button[text() = "Посмотреть статус"]') # Кнопка "Посмотреть статус"

    # Куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Кнопки "Заказать"
    HEADER_ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Header_Nav")]//button[contains(text(), "Заказать")]') # Верхняя кнопка "Закаать"
    BOTTOM_ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Home_FinishButton")]//button[contains(text(), "Заказать")]') # Нижняя кнопка "Заказать"