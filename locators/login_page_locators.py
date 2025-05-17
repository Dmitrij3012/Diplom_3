from selenium.webdriver.common.by import By


class LoginPageLocators:

    FIELD_EMAIL = (
        By.XPATH,
        "//input[@class='text input__textfield text_type_main-default' and @name='name']"
    )

    FIELD_PASSWORD = (
        By.XPATH,
        "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa'
    )

    RECOVERY_PASSWORD_BUTTON = (
        By.XPATH,
        "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
    )

    FIELD_EMAIL_RECOVERY_PASSWORD = (
        By.XPATH,
        "//label[contains(text(), 'Email')]/following-sibling::input"
    )

    RECOVERY_BUTTON = (
        By.CSS_SELECTOR,
        '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa'
    )

    FIELD_PASSWORD_RECOVERY_PASSWORD = (
        By.XPATH,
        "//label[contains(text(), 'Пароль')]/following-sibling::input"
    )

    HIDE_PASSWORD_ICON = (
        By.CSS_SELECTOR,
        '.input__icon.input__icon-action'
    )

    HIDE_PASSWORD_CLASS = (
        By.XPATH,
        "//label[contains(text(), 'Пароль')]/parent::div"
    )

    HIDE_PASSWORD_VALUE = 'input_status_active'

