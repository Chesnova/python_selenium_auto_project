from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert url, "login url is not presented"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "register form is not presented"
        assert True

    # регистрация нового пользователя
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_SUBMIT).click()
