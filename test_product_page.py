from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
import pytest
import time



def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open() # Открываем страницу товара
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE) # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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
    # Открываем страницу товара
    page.open()
    # Добавляем товар в корзину
    page.product_add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    # Открываем страницу товара
    page.open()
    # Добавляем товар в корзину
    page.product_add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() # Проверяем, что перешли на страницу логина

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()

@pytest.mark.new
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
    # открыть страницу регистрации;
    # зарегистрировать нового пользователя;
    # проверить, что пользователь залогинен.
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"  # генерация логина
        password = "fake" + str(time.time())  # генерация пароля
        page_login = LoginPage(browser, link)
        page_login.open()
        page_login.register_new_user(email, password)
        page_login.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        # Открываем страницу товара
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.product_add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_item_name()
        page.check_price()

# pytest -s -v --tb=line test_product_page.py
# @pytest.mark.new
# pytest -s -m "new" test_product_page.py
# pytest -v --tb=line --language=en -m need_review