from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url 

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        password_first = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_rep = self.browser.find_element(*LoginPageLocators.PASSWORD_REP)
        email_reg = self.browser.find_element(*LoginPageLocators.EMAIL)
        button_reg = self.browser.find_element(*LoginPageLocators.REG_BTN)
        email_reg.send_keys(email)
        password_first.send_keys(password)
        password_rep.send_keys(password)
        button_reg.click()
