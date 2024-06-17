import allure

from locators.header_footer_locators import HeaderFooterLocators
from pages.base_page import BasePage


@allure.suite('Общие элементы на страницах, header и footer')
class HeaderFooterPage(BasePage):
    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_to_element(HeaderFooterLocators.SAMOKAT_LOGO)
        return self.driver.current_url

    @allure.step('Переход по логотипу Яндекса')
    def go_to_yandex_from_logo(self):
        self.click_to_element(HeaderFooterLocators.YANDEX_LOGO)
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)

    @allure.step('Проверка наличия логотипа Дзена')
    def is_dzen_logo_displayed(self):
        return self.find_element_with_wait(HeaderFooterLocators.DZEN_LOGO).is_displayed()
