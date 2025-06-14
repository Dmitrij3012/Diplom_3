# Diplom_3
#### <h1>Дипломный проект. Задание 3: веб-приложение</h1>
<hr>

#### <h3>Студент: Дмитрий Соловьев</h2>
#### <h3>Когорта: #18</h2>
<hr>

#### <h1>Тестирование Stellar Burgers</h1>

#### <h2>Инструкция по запуску:</h>

### 1. Установить зависимости:

> pip install -r requirements.txt</h>

### 2. Запустить все тесты и записать отчет:

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по тестированию</h>

> allure serve ./allure-results

<hr>

<h3 align="left">Project files and description:</h3>

| Название файла                     | Содержание файла                   |
|------------------------------------|------------------------------------|
| [allure_results](allure_results)   | Папка с отчетами Allure            | 
| [locators](locators)               | Папка с локаторами                 |
| [pages](pages)                     | Папка с объектами страниц          |
| [methods](methods)                 | Папка с методами                   |
| [tests](tests)                     | Папка с тестами                    |
| [test_password_recovery.py](tests/test_password_recovery.py) | Тесты восстановления пароля        |
| [test_personal_account.py](tests/test_personal_account.py) | Тесты Личного Кабинета             |
| [test_main_functionality.py](tests/test_main_functionality.py) | Тесты основного функционала        |
| [test_order_feed.py](tests/test_order_feed.py) | Тесты раздела "Лента заказов"      |
| [main_page_locators.py](locators/main_page_locators.py) | Локаторы главной страницы          |
| [login_page_locators.py](locators/login_page_locators.py) | Локаторы страницы авторизации      |
| [personal_account_locators.py](locators/personal_account_locators.py) | Локаторы Личного Кабинета          |
| [order_feed_locators.py](locators/order_feed_locators.py) | Локаторы страницы "Лента заказов"  |
| [base_page.py](pages/base_page.py) | Базовые методы                     |
| [main_page.py](pages/main_page.py) | Методы главной страницы                                    |
| [login_page.py](pages/login_page.py) | Методы страницы авторизации        |
| [order_feed_page.py](pages/order_feed_page.py) | Методы страницы "Лента заказов"    |
| [personal_account_page.py](pages/personal_account_page.py) | Методы страницы Личного Кабинета   |
| [auth_methods.py](methods/auth_methods.py) | Метод получения токена             |
| [user_methods.py](methods/user_methods.py) | Методы для работы с пользователями |
| [conftest.py](tests/conftest.py)   | Фикстуры                           |
| [generators.py](generators.py)     | Генераторы данных                  |
| [data.py](data.py)                 | Файл с данными                     |
| [url.py](url.py)                   | Файл с URL                         |
| [requirements.txt](requirements.txt) | Файл с зависимостями               |
