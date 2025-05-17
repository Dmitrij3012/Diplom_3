import allure
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Ввести данные в поле "Email": {keys}')
    def set_email(self, keys):
        self._send_keys_to_input(LoginPageLocators.FIELD_EMAIL, keys)

    @allure.step('Ввести данные в поле "Пароль": {keys}')
    def set_password(self, keys):
        self._send_keys_to_input(LoginPageLocators.FIELD_PASSWORD, keys)

    @allure.step('Кликнуть по кнопке Войти')
    def click_on_login_button(self):
        self._click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Ввести данные в поля "Email": {email} и "Пароль": {password}. Кликнуть по кнопке "Войти"')
    def authorization(self, email, password):
        self._send_keys_to_input(LoginPageLocators.FIELD_EMAIL, email)
        self._send_keys_to_input(LoginPageLocators.FIELD_PASSWORD, password)
        self._click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Кликнуть по кнопке Восстановить пароль')
    def click_on_recovery_password_button(self):
        self._click_on_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Ввести данные в поле "Email" страницы Восстановление пароля: {keys}')
    def set_email_on_recovery_password_page(self, keys):
        self._send_keys_to_input(LoginPageLocators.FIELD_EMAIL_RECOVERY_PASSWORD, keys)

    @allure.step('Кликнуть по кнопке Восстановить')
    def click_on_recovery_button(self):
        self._click_on_element(LoginPageLocators.RECOVERY_BUTTON)

    @allure.step('Ожидание страницы восстановления пароля')
    def waiting_for_password_recovery_page(self):
        self._wait_for_element(LoginPageLocators.FIELD_PASSWORD_RECOVERY_PASSWORD)

    @allure.step('Ввести данные в поле "Пароль" страницы Восстановление пароля: {keys}')
    def set_password_on_recovery_password_page(self, keys):
        self._send_keys_to_input(LoginPageLocators.FIELD_PASSWORD_RECOVERY_PASSWORD, keys)

    @allure.step('Кликнуть по иконке скрыть/показать пароль')
    def click_on_hide_password_button(self):
        # self._wait_for_element_hide(MainPageLocators.OVERLAY)
        self._click_on_element(LoginPageLocators.HIDE_PASSWORD_ICON)

    @allure.step('Получить состояние поля "Пароль"')
    def get_hide_password_element_value(self):
        return self._get_element_value(LoginPageLocators.HIDE_PASSWORD_CLASS, 'class')

    @allure.step('Получить состояние поля "Пароль"')
    def wait_for_load_login_page(self):
        self._wait_for_element(LoginPageLocators.FIELD_EMAIL)
