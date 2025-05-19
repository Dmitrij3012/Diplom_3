import pytest
from selenium import webdriver
from data import Data
from methods.auth_methods import AuthMethods
from methods.user_methods import UserMethods


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    user_data = Data.user_body()
    UserMethods.registration_user(user_data)
    yield user_data
    token = AuthMethods.get_tokens(user_data)
    UserMethods.delete_user(token)
