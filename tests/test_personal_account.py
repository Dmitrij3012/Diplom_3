import allure
import url
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Переход по клику на "Личный кабинет"')
    def test_click_on_personal_account_button(self, driver, create_user):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.authorization(create_user['email'], create_user['password'])

        main_page.click_on_personal_account_button()

        personal_page = PersonalAccountPage(driver)
        personal_page.wait_for_load_page()

        with allure.step('Проверить URL страницы авторизации'):
            assert personal_page._get_url() == url.PERSONAL_ACCOUNT_URL

    @allure.title('Переход перехода в раздел "История заказов"')
    def test_go_to_the_order_history_section(self, driver, create_user):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)

        login_page.authorization(create_user['email'], create_user['password'])
        main_page.click_on_personal_account_button()

        personal_page = PersonalAccountPage(driver)
        personal_page.click_on_order_history_button()

        with allure.step('Проверить URL страницы История заказов'):
            assert personal_page._get_url() == url.ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, create_user):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.authorization(create_user['email'], create_user['password'])

        main_page.click_on_personal_account_button()

        personal_page = PersonalAccountPage(driver)
        personal_page.click_on_logout_button()

        login_page.wait_for_load_login_page()

        with allure.step('Проверить URL страницы авторизации'):
            assert login_page._get_url() == url.LOGIN_URL
