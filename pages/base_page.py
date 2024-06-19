import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.header_footer_locators import HeaderFooterLocators


# Базовые методы, которые будут применяться на каждой странице
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, locator):
        with allure.step(f'Клик по элементу с локатором: {locator}'):
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(locator))
            element.click()

    def get_text_from_element(self, locator):
        with allure.step(f'Получение текста из элемента'
                         f' с локатором: {locator}'):
            element = self.find_element_with_wait(locator)
            return element.text

    # Метод, который форматирует локаторы
    @staticmethod
    def format_locators(locator_template, num):
        method, locator = locator_template
        locator = locator.format(num)
        return method, locator

    @property
    def current_url(self):
        return self.driver.current_url

    @allure.step('Заполняем поле значением')
    def fill(self, locator, value):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located
                                            (locator)).send_keys(value)

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(HeaderFooterLocators.COOKIE_BUTTON)
            )
            cookie_button.click()
        except Exception as e:
            print(f"Cookie button not found or not clickable: {str(e)}")

    @allure.step('Скролл до элемента с локатором {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)

    @allure.step('Ждём и ищем элемент')
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Ждём и ищем элементы')
    def find_elements_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator))

    @allure.step('Скроллим в самый низ')
    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo("
                                   "0, document.body.scrollHeight);")
