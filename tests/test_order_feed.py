import allure
import data
import url
from locators.order_feed_locators import OrderFeedLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:

    @allure.title('Появление всплывающего окна при клике на заказ')
    def test_click_on_order_open_popup(self, driver):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_feed()

        order_feed = OrderFeedPage(driver)
        order_feed.click_on_order()
        value = order_feed.check_window()

        with allure.step('Проверить появление всплывающего окна'):
            assert value == OrderFeedLocators.WINDOW_OPENED_VALUE

    @allure.title('Отображение заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    def test_user_order_from_order_history_and_order_feed(self, driver, create_user):

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
            main_page.close_order_window()

        main_page.click_on_personal_account_button()

        personal_page = PersonalAccountPage(driver)
        personal_page.click_on_order_history_button()

        number_in_order_history = personal_page.get_order_number()
        name_in_order_history = personal_page.get_order_name()

        main_page.click_on_feed()

        order_feed = OrderFeedPage(driver)
        number_in_order_feed = order_feed.get_order_number(number_in_order_history)
        name_in_order_feed = order_feed.get_order_name(name_in_order_history)

        with allure.step('Проверка отображения номера заказа'):
            assert number_in_order_history == number_in_order_feed
        with allure.step('Проверка отображения имени заказа'):
            assert name_in_order_history == name_in_order_feed

    @allure.title('Увеличение счётчика "Выполнено за всё время" при создании заказа')
    def test_number_of_orders_all(self, driver, create_user):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.authorization(create_user['email'], create_user['password'])

        main_page.click_on_feed()

        order_feed = OrderFeedPage(driver)
        count_before_order = order_feed.get_orders_for_all_time()

        main_page.click_on_constructor()

        with allure.step('Создание заказа'):
            main_page.add_ingredient(data.INGREDIENTS[0])
            main_page.add_ingredient(data.INGREDIENTS[1])
            main_page.add_ingredient(data.INGREDIENTS[2])
            main_page.click_on_order_button()
            main_page.close_order_window()

        main_page.click_on_feed()

        count_after_order = order_feed.get_orders_for_all_time()

        with allure.step('Проверить увеличения счётчика'):
            assert int(count_after_order) > int(count_before_order)

    @allure.title('Увеличение счётчика "Выполнено за сегодня" при создании заказа')
    def test_number_of_orders_today(self, driver, create_user):

        main_page = MainPage(driver)
        main_page._load_page(url.MAIN_PAGE_URL)
        main_page.click_on_personal_account_button()

        login_page = LoginPage(driver)
        login_page.authorization(create_user['email'], create_user['password'])

        main_page.click_on_feed()

        order_feed = OrderFeedPage(driver)
        count_before_order = order_feed.get_orders_for_today()

        main_page.click_on_constructor()

        with allure.step('Создание заказа'):
            main_page.add_ingredient(data.INGREDIENTS[0])
            main_page.add_ingredient(data.INGREDIENTS[1])
            main_page.add_ingredient(data.INGREDIENTS[2])
            main_page.click_on_order_button()
            main_page.close_order_window()

        main_page.click_on_feed()

        count_after_order = order_feed.get_orders_for_today()

        with allure.step('Проверить увеличения счётчика'):
            assert int(count_after_order) > int(count_before_order)

    @allure.title('Появление номера заказа в разделе "В работе" после его оформления')
    def test_order_number_in_work_list(self, driver, create_user):

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
            order_number = main_page.get_order_number()
            main_page.close_order_window()

        main_page.click_on_feed()

        order_feed = OrderFeedPage(driver)
        order_feed.wait_order_number_in_work_list(order_number)
        number_in_work_list = order_feed.get_order_number_in_list_in_work_list()

        with allure.step('Проверить появление заказа'):
            assert f'0{order_number}' == number_in_work_list
