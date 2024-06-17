import allure

from helpers import generate_order_info
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


@allure.suite('Тестирование страницы заказа')
class TestOrderPage:

    @allure.title('Тест создания заказа: Первый сценарий')
    @allure.description('Позитивный сценарий создания заказа'
                        ' через верхнюю кнопку')
    def test_create_order_from_header(self, driver, order_info):
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_info = generate_order_info()
        order_info['button'] = MainPageLocators.ORDER_BUTTON_HEADER
        order_page.create_order(order_info)

        assert order_page.check_order_status_window(), (
            "Окно с информацией о заказе не появилось")

    @allure.title('Тест создания заказа: Второй сценарий')
    @allure.description('Позитивный сценарий создания заказа'
                        ' через нижнюю кнопку')
    def test_create_order_from_bottom(self, driver, order_info):
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_info = generate_order_info()
        order_info['button'] = OrderPageLocators.ORDER_BUTTON_ALL_SIZES
        order_page.scroll_page_down()
        order_page.create_order(order_info)

        assert order_page.check_order_status_window(), (
            "Окно с информацией о заказе не появилось")
