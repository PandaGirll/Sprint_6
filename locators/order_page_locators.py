from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    # Поле Имя
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    # Поле Фамилия
    SURNAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    # Поле Адрес
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    # Поле метро
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Локаторы для станций метро
    METRO_STATION_TEMPLATE = '//button[@data-value="{value}"]'
    METRO_STATION_ALL = (By.XPATH, '//*[@class="select-search__option"]')
    METRO_STATION_VISIBLE = (By.XPATH, '//*[@class="select-search__row" '
                                       'and @role="menuitem"]')

    # Поле Телефон
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    # Кнопка Далее
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')

    # Форма "Про аренду"
    # Когда привезти
    DATE_INPUT = (By.XPATH,
                  './/input[@placeholder="* Когда привезти самокат"]')
    DAY_LOCATOR = (By.XPATH,
                   './/div[contains(@class, "react-datepicker__day--today")]')

    # Локатор для Dropdown срока аренды
    RENTAL_DURATION_DROPDOWN = (By.XPATH,
                                '//div[@class="Dropdown-control"]')
    RENTAL_DURATION_OPTION = (By.XPATH,
                              '//div[@class="Dropdown-menu"]//div[text()="{}"]')

    # Цвет самоката
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")

    # Комментарий для курьера
    COMMENT_INPUT = (By.XPATH,
                     "//input[contains(@placeholder, 'Комментарий')]")
    # Кнопка "Заказать"
    MAKE_ORDER_BUTTON = (By.XPATH,
                         '//button[contains(@class, "Button_Middle") '
                         'and contains(text(), "Заказать")]')

    # Локатор для кнопок "Заказать" всех размеров
    ORDER_BUTTON_ALL_SIZES = (By.XPATH,
                              '//div[contains(@class, "Home_FinishButton")]'
                              '/button[contains(@class, "Button_Button") '
                              'and contains(text(), "Заказать")]')

    # Форма подтверждения заказа
    # Кнопка "Да"
    YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button") '
                            'and contains(text(), "Да")]')

    # Окно с информацией о заказе
    STATUS_WINDOW = (By.XPATH, '//div[contains(@class,"Order_ModalHeader")]')
