import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Личный Кабинет"')
    def click_on_personal_account_button(self):
        self._click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликнуть по кнопке "Конструктор"')
    def click_on_constructor(self):
        self._click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_on_feed(self):
        self._click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self, ingredient_id):
        self._click_on_element(MainPageLocators.ingredient(ingredient_id))

    @allure.step('Невидимость окна')
    def window_invisibility(self):
        try:
            self._wait_for_element_hide(MainPageLocators.WINDOW)
            return True
        except TimeoutException:
            return False

    @allure.step('Проверить открытие всплывающего окна')
    def check_window(self):
        return self._get_element_value(MainPageLocators.WINDOW, 'class')

    @allure.step('Закрыть окно')
    def close_window(self):
        self._click_on_element(MainPageLocators.CLOSE_WINDOW_BUTTON)

    @allure.step('Закрыть окно заказа')
    def close_order_window(self):
        self._click_on_element_with_wait_overlay(MainPageLocators.CLOSE_WINDOW_BUTTON,
                                                 'visibility', 'hidden', 'visible')

    @allure.step('Добавить ингредиент')
    def add_ingredient(self, ingredient_id):
        self._drag_and_drop_element(MainPageLocators.ingredient(ingredient_id), MainPageLocators.CONSTRUCTOR_TOP)

    @allure.step('Получить значение счетчика ингредиента')
    def get_count_ingredient(self, ingredient_id):
        return self._get_element_text(MainPageLocators.ingredient_count(ingredient_id))

    @allure.step('Кликнуть по кнопке "Оформить заказ"')
    def click_on_order_button(self):
        self._click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self._get_element_text(MainPageLocators.ORDER_NUMBER)
