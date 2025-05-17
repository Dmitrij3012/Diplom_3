import allure
import data
import url
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunctionality:

    @allure.title('Переход по клику на "Конструктор"')
    @allure.step('Проверка перехода по клику на кнопку "Конструктор"')
    def test_click_on_constructor_button(self, driver):

        main_page = MainPage(driver)
        main_page._load_page(url.LOGIN_URL)
        main_page.click_on_constructor()

        with allure.step('Проверить URL главной страницы'):
            assert main_page._get_url() == url.MAIN_PAGE_URL

    @allure.title('Переход по клику на "Лента Заказов"')
    @allure.step('Проверка перехода по клику на кнопку "Лента Заказов"')
    def test_click_on_feed_button(self, driver):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_feed()

        with allure.step('Проверить URL страницы "Лента Заказов"'):
            assert main_page._get_url() == url.FEED_URL

    @allure.title('Появление всплывающего окна при клике на ингредиент')
    @allure.step('Проверка появления всплывающего окна при клике на ингредиент')
    def test_popup_when_clicked_on_ingredient(self, driver):

        main_page = MainPage(driver)

        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_ingredient(data.INGREDIENTS[0])
        value = main_page.check_window()

        with allure.step('Проверить появление всплывающего окна'):
            assert value == MainPageLocators.WINDOW_OPENED_VALUE

    """ДОРАБОТКА"""
    @allure.title('Закрытие всплывающего окна ингредиента при клике на крестик')
    @allure.step('Проверка закрытие всплывающего окна ингредиента при клике на крестик')
    def test_close_ingredient_window(self, driver):

        main_page = MainPage(driver)

        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_ingredient(data.INGREDIENTS[0])
        main_page.close_window()

        with allure.step('Проверить закрытие всплывающего окна ингредиента'):
            assert main_page.window_invisibility() is True

    @allure.title('Увеличение счетчика ингредиента при его добавлении')
    @allure.step('Проверка увеличения счетчика ингредиента при его добавлении в заказ')
    def test_ingredient_count(self, driver):

        main_page = MainPage(driver)

        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.add_ingredient(data.INGREDIENTS[0])
        value = main_page.get_count_ingredient(data.INGREDIENTS[0])

        with allure.step('Проверить увеличение счетчика ингредиента'):
            assert value == '2'

    @allure.title('Авторизованный пользователь может оформить заказ')
    @allure.step('Проверка оформления заказ с авторизованным пользователем')
    def test_order_with_login(self, driver, create_user):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.authorization(create_user['email'], create_user['password'])

        with allure.step('Создание заказа'):
            main_page.add_ingredient(data.INGREDIENTS[0])
            main_page.add_ingredient(data.INGREDIENTS[1])
            main_page.add_ingredient(data.INGREDIENTS[2])
            main_page.click_on_order_button()
            value = main_page.check_window()

        with allure.step('Проверить создание заказа'):
            assert value == MainPageLocators.WINDOW_OPENED_VALUE
