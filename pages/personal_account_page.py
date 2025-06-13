import allure
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Кликнуть по кнопке "История заказов"')
    def click_on_order_history_button(self):
        self._click_on_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Ожидание загрузки Личного Кабинета')
    def wait_for_load_page(self):
        self._wait_for_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Кликнуть по кнопке "Выход"')
    def click_on_logout_button(self):
        self._click_on_element(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self._get_element_text(PersonalAccountLocators.ORDER_NUMBER)

    @allure.step('Получить имя заказа')
    def get_order_name(self):
        return self._get_element_text(PersonalAccountLocators.ORDER_NAME)
