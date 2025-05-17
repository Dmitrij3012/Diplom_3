from selenium.webdriver.common.by import By


class OrderFeedLocators:

    ORDER = (
        By.XPATH,
        "//ul[@class='OrderFeed_list__OLh59']/li[1]"
    )

    WINDOW = (
        By.XPATH,
        "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']/ancestor::section"
    )

    WINDOW_OPENED_VALUE = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5'

    @staticmethod
    def order_number(number):
        return (
            By.XPATH,
            f'//div[contains(@class, "OrderHistory_textBox__3lgbs mb-6")]'
            f'//p[contains(@class, "text text_type_digits-default") and text()="{number}"]'
        )

    @staticmethod
    def order_name(name):
        return (
            By.XPATH,
            f'//a[contains(@class, "OrderHistory_link__1iNby")]'
            f'//h2[contains(@class, "text text_type_main-medium mb-2") and text()="{name}"]'
        )

    ALL_TIME_COUNT = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//div/p[contains(text(), 'Выполнено за все время:')]"
        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )

    TODAY_COUNT = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//div/p[contains(text(), 'Выполнено за сегодня:')]"
        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )

    LIST_IN_WORK = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//ul[contains(@class, 'orderListReady__1YFem')]/li"
    )
