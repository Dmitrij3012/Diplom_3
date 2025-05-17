import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from config import TIMEOUT_VALUE
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загрузка страницы')
    def _load_page(self, page):
        self.driver.get(page)

    @allure.step('Возврат текущего URL')
    def _get_url(self):
        return self.driver.current_url

    @allure.step('Ожидание невидимости элемента')
    def _wait_for_element_hide(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def _wait_for_element(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def _wait_for_element_clicked(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидание текста внутри элемента')
    def _wait_for_text_in_element(self, locator, text, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Кликнуть на элемент')
    def _click_on_element(self, locator, timeout=TIMEOUT_VALUE):
        self._wait_for_element_hide(MainPageLocators.OVERLAY)
        element = self._wait_for_element_clicked(locator, timeout)
        element.click()

    @allure.step('Ожидание скрытия оверлея по СSS свойству элемента')
    def _waiting_for_window_overlay_to_hide_by_css_property(self, property_name, property_value,
                                                            property_value_2, timeout=TIMEOUT_VALUE):
        def condition(driver):
            element = driver.find_element(*MainPageLocators.OVERLAY)
            return (element.value_of_css_property(property_name) == property_value
                    and element.value_of_css_property(property_name) != property_value_2)

        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step('Кликнуть на элемент c ожиданием скрытия оверлея')
    def _click_on_element_with_wait_overlay(self, locator, property_name, property_value,
                                            property_value_2, timeout=TIMEOUT_VALUE):
        self._waiting_for_window_overlay_to_hide_by_css_property(property_name, property_value, property_value_2)
        element = self._wait_for_element_clicked(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def _send_keys_to_input(self, locator, keys, timeout=TIMEOUT_VALUE):
        element = self._wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить значение элемента')
    def _get_element_value(self, locator, value, timeout=TIMEOUT_VALUE):
        element = self._wait_for_element(locator, timeout)
        return element.get_attribute(value)

    @allure.step('Получить текст элемента')
    def _get_element_text(self, locator, timeout=TIMEOUT_VALUE):
        self._wait_for_element_hide(MainPageLocators.OVERLAY)
        element = self._wait_for_element(locator, timeout)
        return element.text

    @allure.step('Перетащить элемент')
    def _drag_and_drop_element(self, source_locator, target_locator):
        self._wait_for_element_hide(MainPageLocators.OVERLAY)
        source = self._wait_for_element(source_locator)
        target = self._wait_for_element(target_locator)
        drag_and_drop(self.driver, source, target)
