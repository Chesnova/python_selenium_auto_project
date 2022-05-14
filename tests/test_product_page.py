from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.base_page import BasePage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.product_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_item_name()
    page.check_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

# pytest -s -v --tb=line tests/test_product_page.py