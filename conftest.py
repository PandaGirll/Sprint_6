import allure
import pytest
from selenium import webdriver

from data import URLs
from helpers import generate_order_info


# Фикстура драйвера для Google Chrome
@pytest.fixture()
@allure.title("Подготовка драйвера")
def driver():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1920,1080')  # задали р-р окна
    driver = webdriver.Chrome(options=chrome_options)  # инициализируем драйвер
    driver.get(URLs.main_page)  # переходим на основной url
    yield driver  # передаём драйвер в тесты
    driver.quit()  # закрываем драйвер


@pytest.fixture
def order_info():
    return generate_order_info()
