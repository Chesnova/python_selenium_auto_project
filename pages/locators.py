from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_REGISTER_FORM = (By.ID, "register_form")

    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    # поля регистрации нового пользователя
    LOGIN_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    LOGIN_REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    LOGIN_REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    LOGIN_REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')

    # The shellcoder's handbook был добавлен в вашу корзину.
    # Стоимость корзины теперь составляет 9,99 £

