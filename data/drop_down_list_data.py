FAQ_ANSWERS = {
    "cost": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
    "multiple_orders": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
    "rental_time": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
    "order_today": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
    "order_extension": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
    "charger": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
    "order_cancellation": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
    "delivery_outside_mkad": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
}

FAQ_TEST_CASES = [
    {
        "id": "cost",
        "question_locator": "DropDownPageLocators.QUESTION_COST",
        "answer_locator": "DropDownPageLocators.ANSWER_COST",
        "expected_text": FAQ_ANSWERS["cost"]
    },
    {
        "id": "multiple_orders",
        "question_locator": "DropDownPageLocators.QUESTION_MULTIPLE_ORDERS",
        "answer_locator": "DropDownPageLocators.ANSWER_MULTIPLE_ORDERS",
        "expected_text": FAQ_ANSWERS["multiple_orders"]
    },
]
