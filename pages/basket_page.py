from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        try:
            self.browser.find_element(*ProductPageLocators.BASKET_EMPTY_MESSAGE).click()
            result = True
        except NoSuchElementException:
            result = False

        assert result is True, 'Basket is not empty.'