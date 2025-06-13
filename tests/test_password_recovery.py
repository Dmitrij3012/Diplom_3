import allure
import url
from generators import fake_data
from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    def test_go_to_the_password_recovery_page(self, driver):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.click_on_recovery_password_button()

        with allure.step('Проверить URL страницы восстановления пароля'):
            assert login_page._get_url() == url.FORGOT_PASSWORD_URL

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_click_on_the_restore_button(self, driver):

        name, email, password = fake_data()

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.click_on_recovery_password_button()
        login_page.set_email_on_recovery_password_page(email)
        login_page.click_on_recovery_button()
        login_page.waiting_for_password_recovery_page()

        with allure.step('Проверить, что появилось поле ввода нового пароля'):
            assert login_page._get_url() == url.RESET_PASSWORD_URL

    @allure.title('Видимость поля "Пароль"')
    def test_go_to_password_recovery_page(self, driver):

        name, email, password = fake_data()

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.click_on_recovery_password_button()
        login_page.set_email_on_recovery_password_page(email)
        login_page.click_on_recovery_button()
        login_page.set_password_on_recovery_password_page(password)
        login_page.click_on_hide_password_button()
        value = login_page.get_hide_password_element_value()

        with allure.step('Проверить, что при клике по кнопке скрыть/показать пароль поле подсвечивается'):
            assert LoginPageLocators.HIDE_PASSWORD_VALUE in value
