import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть по заказу')
    def click_on_order(self):
        self._click_on_element(OrderFeedLocators.ORDER)

    @allure.step('Проверить открытие всплывающего окна')
    def check_window(self):
        return self._get_element_value(OrderFeedLocators.WINDOW, 'class')

    @allure.step('Получить номер заказа')
    def get_order_number(self, number):
        return self._get_element_text(OrderFeedLocators.order_number(number))

    @allure.step('Получить имя заказа')
    def get_order_name(self, name):
        return self._get_element_text(OrderFeedLocators.order_name(name))

    @allure.step('Получить количество заказов за всё время')
    def get_orders_for_all_time(self):
        return self._get_element_text(OrderFeedLocators.ALL_TIME_COUNT)

    @allure.step('Получить количество заказов за сегодня')
    def get_orders_for_today(self):
        return self._get_element_text(OrderFeedLocators.TODAY_COUNT)

    @allure.step('Получить номер заказа из списка "В работе"')
    def get_order_number_in_list_in_work_list(self):
        return self._get_element_text(OrderFeedLocators.LIST_IN_WORK)

    @allure.step('Ожидание появления номера заказа в списке "В работе"')
    def wait_order_number_in_work_list(self, text):
        self._wait_for_text_in_element(OrderFeedLocators.LIST_IN_WORK, text)
